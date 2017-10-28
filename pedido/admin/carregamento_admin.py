# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin.models import ContentType
from django.contrib.admin.models import LogEntry, CHANGE
from django.forms import TextInput, Textarea
from pedido.models import Carregamento, Item, MotivosAtrasoCarregamento
from grade.models import Grade
from django import forms
from sgo.admin import SgoModelAdmin, SgoTabularInlineAdmin
from django.db import models
from django.forms.models import BaseInlineFormSet
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.http import HttpResponseRedirect
from django.shortcuts import render
from pedido.forms import UpdateDateForm, UpdateGradeForm, AddMotivoCarregamentoForm


class PalletWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        self.qtd_pallets = attrs['qtty']
        attrs['size'] = 5
        widgets = [forms.TextInput(attrs)] * self.qtd_pallets
        super(PalletWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(',')
        return ['']*self.qtd_pallets


class PalletField(forms.fields.MultiValueField):

    def __init__(self, attrs=None):
        self.widget = PalletWidget(attrs)
        fields = [forms.fields.CharField()] * attrs['qtty']
        super(PalletField, self).__init__(fields, attrs)

    def compress(self, values):
        return ','.join(values)


class PedidoCarregamentoAdminForm(forms.ModelForm):

    class Meta:
        model = Carregamento
        fields = "__all__"
        widgets = {
            'hr_grade': TextInput(attrs={'size': 10}),
            'ds_obs_carga': Textarea(attrs={'rows': 4, 'cols': 30}),
        }

    grade = forms.ModelChoiceField(label='Grade do Cliente',queryset=Grade.objects.all(), required=False,)

    def __init__(self, *args, **kwargs):
        super(PedidoCarregamentoAdminForm, self).__init__(*args, **kwargs)
        try:
            self.fields['hr_grade'].widget.attrs['readonly'] = True
            dt_semana = self.instance.dt_saida.weekday()
        except:
            dt_semana = -1
        qt_pallet = self.instance.qt_pallet

        # se a quantidade de pallets = 0 torna invisível o campo de num. de pallets
        if qt_pallet == 0:
            try:
                self.fields['pallets'].widget = forms.HiddenInput()
            except:
                #TODO: When read only mode, throws Key Error here
                pass
        else:
            self.fields['pallets'] = PalletField(attrs={'qtty': qt_pallet,})

        cliente = self.instance.cliente_id
        business_unit = self.instance.business_unit
        grade_queryset = Grade.objects.filter(business_unit__unit=business_unit.unit).filter(dt_semana=dt_semana).filter(cliente_id=cliente).order_by('hr_grade')
        self.fields['grade'].queryset = grade_queryset

    def save(self,commit=True):

        instance = super(PedidoCarregamentoAdminForm, self).save(commit=False)
        # salva a hora do combo da grade no carregamento
        try:
            hora=self.cleaned_data['grade'].hr_grade
            instance.hr_grade= hora
        except:
            # se não selecionar horário de grade , o horário do carregamento continua como está
            pass
        if commit:
            instance.save()
        return instance



class ItemInlineFormSet(BaseInlineFormSet):

    def clean(self):
        """
        Se quantidade faltante>0 exige o preenchimento
        do motivo
        """
        form = None
        for form in self.forms:
            id = form['id'].value()
            item = Item.objects.get(id=id)
            embalagens = int(item.qt_embalagem)
            carregadas = int(form['qt_carregada'].value() or 0)
            falta = embalagens-carregadas
            motivo = form['motivo'].value()
            # Se quantidade em falta for maior do que zero e não tiver
            # nenhum motivo selecionado, mostra mensagem de erro.
            if motivo=='' and falta > 0 and carregadas>0:
                msg = forms.ValidationError("Escolha um motivo.")
                form.add_error('motivo', msg)
            else:
                form.cleaned_data['motivo'] = ''
        super (ItemInlineFormSet, self).clean()
        if form: return form.cleaned_data

# São necessários 2 classes para o mesmo inline devido a permissão de somente leitura
class MotivosAtrasoCarregamentoInline(admin.TabularInline):
    model = MotivosAtrasoCarregamento
    extra = 0
    fields = ['motivo',]

    def is_readonly(self):
       return False

class ItemInline(admin.TabularInline):
    model = Item
    formset = ItemInlineFormSet
    extra = 0
    fields = ['cd_produto','un_embalagem','qt_embalagem','qt_pilha','qt_falta',
             'qt_carregada', 'motivo']
    readonly_fields = ['cd_produto','un_embalagem','qt_embalagem','qt_pilha',
                      'qt_falta', ]
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def is_readonly(self):
        return False

    @property
    def qtd_falta(self):
        return self.instance.qt_embalagem-self.instance.qt_carregada


class ItemInline_ReadOnly(ItemInline):
    readonly_fields = ['cd_produto', 'un_embalagem', 'qt_embalagem', 'qt_pilha',
                       'qt_falta', 'qt_carregada', 'motivo']

    def is_readonly(self):
        return True


class PedidoCarregamentoAdmin(SgoModelAdmin):

    form = PedidoCarregamentoAdminForm
    template_name = 'pedido/add_date.html'
    actions=['set_chegada', 'set_inicio', 'set_fim', 'set_libera', 'add_motivo_atraso']

    def save_model(self, request, obj, form, change):
        obj.save()

    def has_add_permission(self, request):
        return False

    def add_log_carregamento(self, request, queryset, obj):
        ct = ContentType.objects.get_for_model(queryset.model)
        LogEntry.objects.log_action(  # log_entry --> log_action
            user_id=request.user.id,
            content_type_id=ct.pk,
            object_id=obj.pk,
            object_repr=''.join([obj.cliente.nm_ab_cli, obj.nr_nota_fis]),
            action_flag=CHANGE,  # actions_flag --> action_flag
            change_message='Modificado Status para ' + obj.STATUS[obj.ds_status_carrega][1])

    def add_motivo_atraso(self, request, queryset):
        """ Para cada carregamento selecionado, adiciona um motivo de atraso do caminhão,
        e um comentário para o motivo quando necessário.
        """
        template_name = 'pedido/add_motivo.html'
        form = None
        action_name = 'add_motivo_atraso'

        if 'apply' in request.POST:
            form = AddMotivoCarregamentoForm(request.POST)
            if form.is_valid():

                for c in queryset:
                    motivo = form.cleaned_data['motivo']
                    ds_obs = form.cleaned_data['ds_obs']
                    c.add_motivo_atraso(motivo, ds_obs)

                    # adiciona evento no log
                    self.add_log_carregamento(request, queryset, c)
                    # save event
                    c.save()
                rows_updated = queryset.count()

                if rows_updated == 1:
                    message_bit = "1 carregamento foi"
                else:
                    message_bit = "%s carregamentos foram" % rows_updated
                self.message_user(request, "%s adicionado(s) um motivo de atraso." % message_bit)
                return HttpResponseRedirect(request.get_full_path())
        if not form:
            form = AddMotivoCarregamentoForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        context = {
            'queryset': queryset,
            'form': form,
            'action_name': action_name
        }

        return render(request, template_name, context)
    add_motivo_atraso.short_description = 'Adicionar motivo de atraso'

    def set_chegada(self, request, queryset):
        """ Para cada carregamento selecionado, seta a hora de chegada do caminhão,
        A placa do veículo e o número do lacre caso existam
        campos em branco, informação não é alterada."""

        form = None
        action_name = 'set_chegada'

        if 'apply' in request.POST:
            form = UpdateGradeForm(request.POST)
            if form.is_valid():

                for c in queryset:
                    date = form.cleaned_data['data']
                    grade = form.cleaned_data['grade']
                    placa = form.cleaned_data['ds_placa']
                    lacre = form.cleaned_data['nr_lacre']
                    c.set_chegada(date, grade, placa, lacre)

                    # adiciona evento no log
                    self.add_log_carregamento(request, queryset, c)
                    # save event
                    c.save()
                rows_updated = queryset.count()

                if rows_updated == 1:
                    message_bit = "1 carregamento foi"
                else:
                    message_bit = "%s carregamentos foram" % rows_updated
                self.message_user(request, "%s marcado(s) como caminhão na planta." % message_bit)
                return HttpResponseRedirect(request.get_full_path())
        if not form:
            form = UpdateGradeForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        context = {
            'queryset': queryset,
            'form': form,
            'action_name': action_name
        }

        return render(request, self.template_name, context)
    set_chegada.short_description = 'Sinalizar chegada do caminhão'

    def set_inicio(self, request, queryset):
        form = None
        action_name = 'set_inicio'
        if 'apply' in request.POST:
            form = UpdateDateForm(request.POST)
            if form.is_valid():
                # Para cada carregamento selecionado, seta a hora de chegada do caminhão
                for c in queryset:
                    date = form.cleaned_data['data']
                    placa = form.cleaned_data['ds_placa']
                    lacre = form.cleaned_data['nr_lacre']
                    c.set_inicio(date, placa, lacre)
                    # adiciona evento no log
                    self.add_log_carregamento(request, queryset, c)
                    # save event
                    c.save()
                rows_updated = queryset.count()

                if rows_updated == 1:
                    message_bit = "1 carregamento foi"
                else:
                    message_bit = "%s carregamentos foram" % rows_updated
                self.message_user(request, "%s marcado(s) como iniciado(s)." % message_bit)
                return HttpResponseRedirect(request.get_full_path())
        if not form:
            form = UpdateDateForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        context = {
            'queryset': queryset,
            'form': form,
            'action_name': action_name,
        }

        return render(request, self.template_name, context)
    set_inicio.short_description = 'Sinalizar início do carregamento'

    def set_fim(self, request, queryset):
        form = None
        action_name = 'set_fim'
        if 'apply' in request.POST:
            form = UpdateDateForm(request.POST)
            if form.is_valid():
                # Para cada carregamento selecionado, seta a hora de chegada do caminhão
                for c in queryset:
                    date = form.cleaned_data['data']
                    placa = form.cleaned_data['ds_placa']
                    lacre = form.cleaned_data['nr_lacre']
                    c.set_fim(date, placa, lacre)
                    # adiciona evento no log
                    self.add_log_carregamento(request, queryset, c)
                    # save event
                    c.save()
                rows_updated = queryset.count()

                if rows_updated == 1:
                    message_bit = "1 carregamento foi"
                else:
                    message_bit = "%s carregamentos foram" % rows_updated
                self.message_user(request, "%s marcado(s) como finalizado(s)." % message_bit)
                return HttpResponseRedirect(request.get_full_path())
        if not form:
            form = UpdateDateForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        context = {
            'queryset': queryset,
            'form': form,
            'action_name': action_name,
        }

        return render(request, self.template_name, context)
    set_fim.short_description = 'Sinalizar fim do carregamento'

    def set_libera(self, request, queryset):
        form = None
        action_name = 'set_libera'
        if 'apply' in request.POST:
            form = UpdateDateForm(request.POST)
            if form.is_valid():
                # Para cada carregamento selecionado, seta a hora de chegada do caminhão
                for c in queryset:
                    date = form.cleaned_data['data']
                    placa = form.cleaned_data['ds_placa']
                    lacre = form.cleaned_data['nr_lacre']
                    c.set_libera(date, placa, lacre)
                    # adiciona evento no log
                    self.add_log_carregamento(request, queryset, c)
                    # save event
                    c.save()
                rows_updated = queryset.count()

                if rows_updated == 1:
                    message_bit = "1 carregamento foi"
                else:
                    message_bit = "%s carregamentos foram" % rows_updated
                self.message_user(request, "%s marcado(s) como caminhão liberado." % message_bit)
                return HttpResponseRedirect(request.get_full_path())
        if not form:
            form = UpdateDateForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        context = {
            'queryset': queryset,
            'form': form,
            'action_name': action_name,
        }

        return render(request, self.template_name, context)
    set_libera.short_description = 'Sinalizar liberação do caminhão'

    def get_classe_cli(self,obj):
        return obj.cliente.ds_classe_cli


    def carregamento_motivos(self):
        pass 

    get_classe_cli.short_description = 'Canal Cliente'
    get_classe_cli.admin_order_field = 'cliente__ds_classe_cli'

    inlines = [MotivosAtrasoCarregamentoInline, ItemInline, ItemInline_ReadOnly]
    verbose_name = ('Pedido')

    list_display = ('id', 'nr_nota_fis', 'nr_pedido', 'ds_ord_compra', 'business_unit','dt_saida', 'hr_grade',
                    'cliente', 'get_classe_cli', 'ds_transp', 'cd_rota', 'ds_status_cheg', 'ds_status_lib','ds_status_carrega' )
    readonly_fields = ('ds_status_cheg', 'ds_status_lib', 'cliente', 'ds_status_carrega', 'business_unit',
                       'ds_transp', 'cd_rota', 'nr_nota_fis', 'nr_pedido', 'ds_ord_compra',
                       'dt_hr_chegada', 'dt_hr_ini_carga', 'dt_hr_fim_carga', 'dt_hr_liberacao')

    fieldsets = (
        (None, {'fields':(
                        ('business_unit','cliente','nr_nota_fis', 'nr_pedido', 'ds_ord_compra',),
                        ('dt_saida','hr_grade', 'grade'),
                        ('ds_transp', 'ds_placa','nr_lacre'),
                        ('ds_status_carrega','ds_status_cheg','ds_status_lib',),
                        ('ds_obs_carga','qt_pallet', 'pallets','cd_rota'),
                        )
                }),
        ('Acompanhamento do Carregamento',{
            'classes':('collapse',),
                'fields':(('dt_hr_chegada','dt_hr_ini_carga','dt_hr_fim_carga', 'dt_hr_liberacao'))
        })
    )
    list_filter = (('dt_saida', DateRangeFilter), 'business_unit', 'ds_status_carrega', 'cd_rota','cliente__ds_classe_cli',
                   'ds_transp', 'carregamento_motivo__motivo')

    search_fields = ['nr_nota_fis','cliente__nm_ab_cli' ,]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(Carregamento, PedidoCarregamentoAdmin)
