# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.forms import TextInput
from pedido.models import Carregamento, Item
from grade.models import Grade
from django import forms
from multa.models import MultaCarregamento, MultaItem
from sgo.admin import SgoModelAdmin, SgoTabularInlineAdmin


class PedidoItemAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"


class PedidoItemAdmin(SgoModelAdmin):

    form = PedidoItemAdminForm
    verbose_name = ('Itens do Pedido')


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
        self.fields['hr_grade'].widget.attrs['readonly'] = True
        try:
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

# São necessários 2 classes para o mesmo inline devido a permissão de somente leitura

class ItemInline(SgoTabularInlineAdmin):
    model = Item
    extra = 0
    fields = ['nr_nota_fis', 'ds_ord_compra', 'cd_produto','un_embalagem','qt_embalagem','qt_pilha','qt_falta',
              'qt_carregada', 'motivo']
    readonly_fields = ['nr_nota_fis','cd_produto','un_embalagem','qt_embalagem','qt_pilha', 'ds_ord_compra',
                       'qt_falta', ]

    def has_add_permission(self, request):
        return False

    def multa(self, obj):
        print(obj.multa)
        if obj.multa:
            return '<a href="/multa/multa_item/'+str(obj.multa)+'/">Ver/editar multa</a>'
        else:
            return '<a href="/multa/multa_item/add/">Adicionar multa</a>'
        multa.allow_tags = True

    def has_delete_permission(self, request, obj=None):
        return False

    def is_readonly(self):
        return False


class ItemInline_ReadOnly(ItemInline):
    model = Item
    extra = 0

    def is_readonly(self):
        return True

    def detalhe(self, obj):
        return '<a href="/multa/multaitem/add/">Ver detalhes</a>'
    detalhe.allow_tags = True


class MultaItemInline(SgoTabularInlineAdmin):
    model = MultaItem
    extra = 0
    fields = ['vl_base_multa', 'vl_multa',]

    def is_readonly(self):
        return False

    def clean_vl_base_multa(self):
        data = self.cleaned_data['vl_base_multa']
        data = '${:,.2f}'.format(data)
        return data


class MultaItemInline_ReadOnly(SgoTabularInlineAdmin):
    model = MultaItem
    extra = 0
    fields = ['vl_base_multa', 'vl_multa',]

    def is_readonly(self):
        return True

class MultaCarregamentoInline(SgoTabularInlineAdmin):
    model = MultaCarregamento
    extra = 0
    fields = ['vl_base_multa', 'vl_fixo', 'vl_multa',]

    def is_readonly(self):
        return False


class MultaCarregamentoInline_ReadOnly(SgoTabularInlineAdmin):
    model = MultaCarregamento
    extra = 0
    fields = ['vl_base_multa', 'vl_fixo', 'vl_multa',]

    def is_readonly(self):
        return True


class EstabListFilter(admin.SimpleListFilter):
    title = ('estabelecimento')
    parameter_name = 'estabelecimento'
    default_value = None


class PedidoCarregamentoAdmin(SgoModelAdmin):
    form = PedidoCarregamentoAdminForm

    def has_add_permission(self, request):
        return False

    def set_chegada(self, request, queryset):
        # Para cada carregamento selecionado, seta a hora de chegada do caminhão
        for c in queryset:
            c.set_chegada() #carregamento=c)
        rows_updated = queryset.update(ds_status_carrega=Carregamento.NA_PLANTA,)
        if rows_updated == 1:
            message_bit = "1 carregamento foi"
        else:
            message_bit = "%s carregamentos foram" % rows_updated
        self.message_user(request, "%s marcados como caminhão na planta." % message_bit)
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
        self.message_user(request, "%s marcados como iniciado(s)." % message_bit)
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
        self.message_user(request, "%s marcados como finalizado(s)." % message_bit)
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
        self.message_user(request, "%s marcados como caminhão liberado." % message_bit)
    set_libera.short_description='Sinalizar liberação do caminhão'

    actions=[set_chegada, set_inicio, set_fim, set_libera]

    inlines = [ItemInline_ReadOnly, ItemInline, ]
    verbose_name = ('Pedido')
    list_display = ('business_unit','nr_nota_fis','dt_saida', 'hr_grade', 'cliente', 'business_unit', 'ds_transp','ds_status_carrega' )
    readonly_fields = ('ds_status_cheg', 'ds_status_lib', 'cliente', 'ds_status_carrega', 'business_unit', 'ds_transp',) #'hr_grade',)

    fieldsets = (
        (None, {'fields':(
                          ('business_unit','cliente','dt_saida','hr_grade', 'grade'),
                        ('ds_transp', 'ds_placa','nr_lacre'),
                        ('ds_status_carrega','ds_status_cheg','ds_status_lib',),
                        ('ds_obs_carga'),
                        ('qt_pallet'))
                }),
        ('Acompanhamento do Carregamento',{
            'classes':('collapse',),
                'fields':(('dt_hr_chegada','dt_hr_ini_carga','dt_hr_fim_carga', 'dt_hr_liberacao'))
        })
    )
    #readonly_fields = ('business_unit','nm_ab_cliente','nr_nota_fis','nr_pedido','dt_atlz',)
    list_filter = ('business_unit','ds_status_carrega',) #'nm_ab_cli') #'[EstabListFilter,]
    search_fields = ['nr_nota_fis','cliente__nm_ab_cli' ,]


class FillRate(Item):
    class Meta:
        proxy = True

class FillRateAdmin(PedidoItemAdmin):
    verbose_name = "Fill Rate"
    list_display = ('business_unit', 'cliente', 'nr_nota_fis', 'ds_ord_compra', 'nr_pedido', 'cd_produto',  'qt_falta',
                    'motivo',)

    readonly_fields = ('business_unit', 'cliente', 'nr_nota_fis', 'ds_ord_compra', 'nr_pedido', 'cd_produto',  'qt_falta',
                       'un_embalagem', 'qt_embalagem', 'qt_pilha', 'qt_carregada', 'ds_produto', )
    inlines = [MultaItemInline, MultaItemInline_ReadOnly]
    fieldsets = (
        (None,{'fields':(
            (('business_unit', 'cliente'), ('nr_nota_fis', 'ds_ord_compra', 'nr_pedido',),
             ('cd_produto','ds_produto'), ('un_embalagem', 'qt_embalagem', 'qt_pilha'),
             ('qt_falta', 'qt_carregada',))),
    }),)
    list_filter = ('business_unit', 'cliente__nm_ab_cli',)
    search_fields = ['nr_nota_fis', 'nr_pedido', 'ds_ord_compra' ,]

    def get_queryset(self, request):
        qs = super(FillRateAdmin, self).get_queryset(request)
        return qs

    def has_add_permission(self, request):
        return False


class NoShow(Carregamento):
    class Meta:
        proxy = True

class NoShowAdmin(PedidoCarregamentoAdmin):
    verbose_name = "No Show"
    list_display = (
        'business_unit', 'cliente', 'nr_nota_fis', 'dt_saida', 'hr_grade', 'ds_status_carrega', 'ds_status_cheg',
        'ds_status_lib', 'id_no_show', )
    list_filter = ()
    readonly_fields = ('business_unit', 'cliente', 'dt_saida', 'ds_transp', )
    inlines = [MultaCarregamentoInline, MultaCarregamentoInline_ReadOnly]
    fieldsets = (
        (None, {'fields': (
            ('business_unit', 'cliente'), ('dt_saida', 'hr_grade', ),
            ('ds_transp', 'id_no_show'))
        }),
    )

    def get_queryset(self, request):
        qs = super(NoShowAdmin, self).get_queryset(request)
        return qs.filter(id_no_show=Carregamento.SIM)

    def has_add_permission(self, request):
        return False

    def clean_vl_base_multa(self):
        data = self.cleaned_data['vl_base_multa']
        data = '${:,.2f}'.format(data)
        return data


admin.site.register(Carregamento, PedidoCarregamentoAdmin)
admin.site.register(FillRate, FillRateAdmin)
admin.site.register(NoShow, NoShowAdmin)
#admin.site.register(Item, PedidoItemAdmin)
