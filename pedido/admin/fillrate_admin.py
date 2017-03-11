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
    fields = ['vl_multa',] #'vl_base_multa' excluido iss#34

    def is_readonly(self):
        return False


class MultaItemInline_ReadOnly(MultaItemInline):

    readonly_fields = ['vl_multa',]

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
    list_display = ('get_nota_fiscal', 'get_pedido', 'get_ordem_compra', 'business_unit', 'get_cliente', 'cd_produto',
                    'qt_falta', 'motivo', 'total_multas')

    readonly_fields = ('business_unit', 'get_cliente', 'get_nota_fiscal', 'get_ordem_compra',
                       'get_pedido', 'cd_produto', 'qt_falta',
                       'un_embalagem', 'qt_embalagem', 'qt_pilha', 'qt_carregada', 'ds_produto', 'motivo' )
    inlines = [MultaItemInline, MultaItemInline_ReadOnly]
    fieldsets = (
        (None,{'fields':(
            (('business_unit', 'get_cliente'), ('get_nota_fiscal', 'get_ordem_compra', 'get_pedido',),
             ('cd_produto','ds_produto'), ('un_embalagem', 'qt_embalagem', 'qt_pilha'),
             ('qt_falta', 'qt_carregada','motivo'))),
    }),)
    list_filter = ['business_unit', FillRateListFilter, ]

    search_fields = ['carregamento__nr_nota_fis', 'carregamento__nr_pedido', 'carregamento__ds_ord_compra',
                     'cliente__nm_ab_cli'
                     ]

    def get_nota_fiscal(self, obj):
        return obj.carregamento.nr_nota_fis

    def get_cliente(self, obj):
        return obj.carregamento.cliente.nm_ab_cli

    def get_ordem_compra(self, obj):
        return obj.carregamento.ds_ord_compra

    def get_pedido(self, obj):
        return obj.carregamento.nr_pedido

    def total_multas(self, obj):
        multas = [k.vl_multa for k in obj.item_multa.all()]
        return sum(multas)

    def get_queryset(self, request):
        qs = super(FillRateAdmin, self).get_queryset(request)
        return qs

    def has_add_permission(self, request):
        return False

    get_nota_fiscal.admin_order_field  = 'carregamento__nr_nota_fis'  #Allows column order sorting
    get_nota_fiscal.short_description = 'Nota Fiscal'  #Renames column head
    get_ordem_compra.admin_order_field  = 'carregamento__ds_ord_compra'
    get_ordem_compra.short_description = 'Ordem Compra'
    get_pedido.admin_order_field  = 'carregamento__nr_pedido'
    get_pedido.short_description = 'Pedido'

admin.site.register(FillRate, FillRateAdmin)
