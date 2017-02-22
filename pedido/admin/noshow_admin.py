# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from pedido.models import NoShow
from multa.models import MultaCarregamento
from sgo.admin import SgoTabularInlineAdmin, SgoModelAdmin
from django import forms


class NoShowAdminForm(forms.ModelForm):
    class Meta:
        model = NoShow
        fields = "__all__"


class MultaCarregamentoInline(SgoTabularInlineAdmin):
    model = MultaCarregamento
    extra = 0
    fields = ['vl_multa',] #'vl_base_multa', 'vl_fixo' excluidos iss#34

    def is_readonly(self):
        return False


class MultaCarregamentoInline_ReadOnly(MultaCarregamentoInline):
    readonly_fields = ['vl_multa',]

    def is_readonly(self):
        return True


class NoShowListFilter(SimpleListFilter):
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
            return queryset.filter(carregamento_multa__gt=0).distinct()
        elif self.value() == None:
            return queryset.filter(carregamento_multa__gt=0).distinct()


class NoShowAdmin(SgoModelAdmin):
    form = NoShowAdminForm
    actions = None
    verbose_name = "No Show"
    list_display = ('nr_nota_fis', 'nr_pedido', 'ds_ord_compra',
        'business_unit', 'cliente', 'dt_saida', 'hr_grade', 'ds_status_carrega', 'ds_status_cheg',
        'ds_status_lib', 'total_multas', 'id_no_show', )
    list_filter = ['business_unit', NoShowListFilter,]
    readonly_fields = ('business_unit', 'cliente', 'dt_saida', 'ds_transp','nr_nota_fis', 'nr_pedido', 'ds_ord_compra',)
    inlines = [MultaCarregamentoInline, MultaCarregamentoInline_ReadOnly]
    fieldsets = (
        (None, {'fields': (
            ('nr_nota_fis', 'nr_pedido', 'ds_ord_compra',),
            ('business_unit', 'cliente'), ('dt_saida', 'hr_grade', ),
            ('ds_transp', 'id_no_show'))
        }),
    )
    search_fields = ['nr_nota_fis', 'cliente__nm_ab_cli', 'nr_pedido', 'ds_ord_compra']
    def get_queryset(self, request):
        qs = super(NoShowAdmin, self).get_queryset(request)
        return qs

    def total_multas(self, obj):
        multas = [k.vl_multa for k in obj.carregamento_multa.all()]
        return sum(multas)

    def has_add_permission(self, request):
        return False



admin.site.register(NoShow, NoShowAdmin)
