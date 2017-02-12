# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.forms import TextInput, Textarea
from pedido.models import Carregamento, Item
from grade.models import Grade
from django import forms
from sgo.admin import SgoModelAdmin, SgoTabularInlineAdmin
from django.db import models
from django.forms.models import BaseInlineFormSet

class PedidoCarregamentoAdminForm(forms.ModelForm):
    class Meta:
        model = Carregamento
        fields = "__all__"
        widgets = {
            'hr_grade': TextInput(attrs={'size': 10}),
        }

    grade = forms.ModelChoiceField(label='Grade do Cliente',queryset=Grade.objects.all(), required=False,)

    def __init__(self, *args, **kwargs):
        super(PedidoCarregamentoAdminForm, self).__init__(*args, **kwargs)

        try:
            self.fields['hr_grade'].widget.attrs['readonly'] = True
            dt_semana = self.instance.dt_saida.weekday()
        except:
            dt_semana = -1
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
    """
    Se quantidade faltante>0 exige o preenchimento
    do motivo
    """
    def clean(self):
        for form in self.forms:
            id = form['id'].value()
            item = Item.objects.get(id=id)
            embalagens = int(item.qt_embalagem)
            carregadas = int(form['qt_carregada'].value())
            falta = embalagens-carregadas
            #print('carregadas',carregadas, ' - ', 'embalagens', embalagens, ' - ','falta', falta)
            motivo = form['motivo'].value()
            # print('motivo',motivo, ' - ', 'falta', falta, motivo=='' , falta>0)
            # Se quantidade em falta for maior do que zero e não tiver
            # nenhum motivo selecionado, mostra mensagem de erro.
            if motivo=='' and falta > 0 and carregadas>0:
                msg = forms.ValidationError("Escolha um motivo.")
                form.add_error('motivo', msg)
            else:
                form.cleaned_data['motivo'] = ''
        #super (ItemInlineFormSet, self).clean()
        #return form.cleaned_data

# São necessários 2 classes para o mesmo inline devido a permissão de somente leitura


class ItemInline(SgoTabularInlineAdmin):
    model = Item
    formset = ItemInlineFormSet
    extra = 0
    fields = ['nr_nota_fis', 'ds_ord_compra', 'cd_produto','un_embalagem','qt_embalagem','qt_pilha','qt_falta',
              'qt_carregada', 'motivo']
    readonly_fields = ['nr_nota_fis','cd_produto','un_embalagem','qt_embalagem','qt_pilha', 'ds_ord_compra',
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
    readonly_fields = ['nr_nota_fis', 'cd_produto', 'un_embalagem', 'qt_embalagem', 'qt_pilha', 'ds_ord_compra',
                       'qt_falta', 'qt_carregada', 'motivo']

    def is_readonly(self):
        return True


class PedidoCarregamentoAdmin(SgoModelAdmin):
    form = PedidoCarregamentoAdminForm

    def is_proxy(self):
        print (dir(self))
        return True

    def save_model(self, request, obj, form, change):
        obj.save()

    def has_add_permission(self, request):
        return False

    def set_chegada(self, request, queryset):
        # Para cada carregamento selecionado, seta a hora de chegada do caminhão
        for c in queryset:
            c.set_chegada()
        rows_updated = queryset.update(ds_status_carrega=Carregamento.NA_PLANTA,)
        if rows_updated == 1:
            message_bit = "1 carregamento foi"
        else:
            message_bit = "%s carregamentos foram" % rows_updated
        self.message_user(request, "%s marcado(s) como caminhão na planta." % message_bit)
    set_chegada.short_description='Sinalizar chegada do caminhão'

    def set_inicio(self, request, queryset):
        # Para cada carregamento selecionado, seta a hora de início do carregamento
        for c in queryset:
            c.set_inicio()
        rows_updated = queryset.update(ds_status_carrega=Carregamento.INICIO,)
        if rows_updated == 1:
            message_bit = "1 carregamento foi"
        else:
            message_bit = "%s carregamentos foram" % rows_updated
        self.message_user(request, "%s marcado(s) como iniciado(s)." % message_bit)
    set_inicio.short_description='Sinalizar início do carregamento'

    def set_fim(self, request, queryset):
        # Para cada carregamento selecionado, seta a hora de fim do carregamento
        for c in queryset:
            c.set_fim()
        rows_updated = queryset.update(ds_status_carrega=Carregamento.FIM,)
        if rows_updated == 1:
            message_bit = "1 carregamento foi"
        else:
            message_bit = "%s carregamentos foram" % rows_updated
        self.message_user(request, "%s marcado(s) como finalizado(s)." % message_bit)
    set_fim.short_description='Sinalizar fim do carregamento'

    def set_libera(self, request, queryset):
        # Para cada carregamento selecionado, seta a hora de liberação do caminhão
        for c in queryset:
            c.set_libera() #carregamento=c)
        rows_updated = queryset.update(ds_status_carrega=Carregamento.LIBERADO,)
        if rows_updated == 1:
            message_bit = "1 carregamento foi"
        else:
            message_bit = "%s carregamentos foram" % rows_updated
        self.message_user(request, "%s marcado(s) como caminhão liberado." % message_bit)

    set_libera.short_description='Sinalizar liberação do caminhão'

    actions=[set_chegada, set_inicio, set_fim, set_libera]

    inlines = [ ItemInline, ItemInline_ReadOnly, ]
    verbose_name = ('Pedido')
    list_display = ('nr_nota_fis', 'business_unit','dt_saida', 'hr_grade', 'cliente', 'ds_transp','ds_status_cheg', 'ds_status_lib','ds_status_carrega' )
    readonly_fields = ('ds_status_cheg', 'ds_status_lib', 'cliente', 'ds_status_carrega', 'business_unit', 'ds_transp',) #'hr_grade',)

    fieldsets = (
        (None, {'fields':(
                        ('business_unit','cliente','dt_saida','hr_grade', 'grade'),
                        ('ds_transp', 'ds_placa','nr_lacre'),
                        ('ds_status_carrega','ds_status_cheg','ds_status_lib',),
                        ('ds_obs_carga','qt_pallet',),
                        )
                }),
        ('Acompanhamento do Carregamento',{
            'classes':('collapse',),
                'fields':(('dt_hr_chegada','dt_hr_ini_carga','dt_hr_fim_carga', 'dt_hr_liberacao'))
        })
    )
    #readonly_fields = ('business_unit','nm_ab_cliente','nr_nota_fis','nr_pedido','dt_atlz',)
    list_filter = ('business_unit','ds_status_carrega',) #'nm_ab_cli') #'[EstabListFilter,]
    search_fields = ['nr_nota_fis','cliente__nm_ab_cli' ,]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(Carregamento, PedidoCarregamentoAdmin)
