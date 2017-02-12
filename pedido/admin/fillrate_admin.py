# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from pedido.models import Item, FillRate
from django import forms
from multa.models import MultaItem
from sgo.admin import SgoModelAdmin, SgoTabularInlineAdmin

class PedidoItemAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

class PedidoItemAdmin(SgoModelAdmin):

    form = PedidoItemAdminForm
    verbose_name = ('Itens do Pedido')


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


class MultaItemInline_ReadOnly(MultaItemInline):

    readonly_fields = ['vl_base_multa', 'vl_multa',]

    def is_readonly(self):
        return True


class FillRateListFilter(SimpleListFilter):
    title = ('status')
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (('multados', ('Multados')),('todos', ('Todos')),)

    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value() == 'multados':
            return queryset.filter(item_multa__gt=0).distinct()
        elif self.value() == None:
            return queryset.filter(item_multa__gt=0).distinct()


class FillRateAdmin(SgoModelAdmin):
    verbose_name = "Fill Rate"
    list_display = ('nr_nota_fis', 'ds_ord_compra', 'nr_pedido', 'business_unit', 'cliente', 'cd_produto',  'qt_falta',
                    'motivo','total_multas')

    readonly_fields = ('business_unit', 'cliente', 'nr_nota_fis', 'ds_ord_compra', 'nr_pedido', 'cd_produto',  'qt_falta',
                       'un_embalagem', 'qt_embalagem', 'qt_pilha', 'qt_carregada', 'ds_produto', 'motivo' )
    inlines = [MultaItemInline, MultaItemInline_ReadOnly]
    fieldsets = (
        (None,{'fields':(
            (('business_unit', 'cliente'), ('nr_nota_fis', 'ds_ord_compra', 'nr_pedido',),
             ('cd_produto','ds_produto'), ('un_embalagem', 'qt_embalagem', 'qt_pilha'),
             ('qt_falta', 'qt_carregada','motivo'))),
    }),)
    list_filter = ['business_unit', FillRateListFilter, ]

    search_fields = ['nr_nota_fis', 'nr_pedido', 'ds_ord_compra', 'cliente__nm_ab_cli']

    def total_multas(self, obj):
        multas = [k.vl_multa for k in obj.item_multa.all()]
        return sum(multas)

    def get_queryset(self, request):
        qs = super(FillRateAdmin, self).get_queryset(request)
        return qs

    def has_add_permission(self, request):
        return False


admin.site.register(FillRate, FillRateAdmin)
