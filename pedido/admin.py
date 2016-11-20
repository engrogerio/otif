# -*- encoding: utf-8 -*-

from django.contrib import admin
from pedido.models import Base, Item
from grade.models import Grade
from cliente.models import Cliente
from django import forms
from django.db.models import Func


# Register your models here.

class PedidoBaseAdminForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = "__all__"

    def __init__(self, *args, **kwds):
        super(PedidoBaseAdminForm, self).__init__(*args, **kwds)
        cli=self.instance.cliente
        if self.instance.grade:
            grade = Grade.objects.order_by(Func('hr_grade_seg', function='"time"'))
            self.fields['grade'].queryset = grade

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    fields = ['nr_nota_fis','cd_produto','un_embalagem','qt_embalagem','qt_pilha','qt_falta', 'qt_carregada', 'qt_pallet', 'adicionar_multa']
    readonly_fields = ['nr_nota_fis','cd_produto','un_embalagem','qt_embalagem','qt_pilha', 'adicionar_multa']

    def adicionar_multa(self, obj):
        return '<a href="/pedido/item/'+str(obj.id)+'/">Ver Ítem</a>'

    adicionar_multa.allow_tags = True


# class PedidoItemInline(admin.TabularInline):
#     extra = 0
#     model = Base.item.through
#     #fields = ['qt_carregada', ]
#     readonly_fields = ['nr_nota_fis','cd_produto','un_embalagem','qt_embalagem','qt_pilha','qt_falta',
#                         'qt_pallet']
#     exclude = ('item',)
#
#     def nr_nota_fis(self, instance):
#         return instance.item.nr_nota_fis
#
#     def cd_produto(self, instance):
#         return instance.item.cd_produto
#
#     def un_embalagem(self, instance):
#         return instance.item.un_embalagem
#
#     def qt_embalagem(self, instance):
#         return instance.item.qt_embalagem
#
#     def qt_pilha(self, instance):
#         return instance.item.qt_pilha
#
#     def qt_carregada(self, instance):
#         return instance.item.qt_carregada
#
#     def qt_falta(self, instance):
#         return instance.item.qt_falta
#
#     def qt_pallet(self, instance):
#         return instance.item.qt_pallet
#
#     cd_produto.short_description = 'código do produto'
#
#     #fields = ('nr_nota_fis','cd_produto','un_embalagem','qt_embalagem','qt_pilha','qt_carregada','qt_falta','qt_pallet')
#     #readonly_fields = ('nr_nota_fis','cd_produto','un_embalagem','qt_embalagem','qt_pilha')

class EstabListFilter(admin.SimpleListFilter):
    title = ('estabelecimento')
    parameter_name = 'estabelecimento'
    default_value = None


    # def lookups(self, request, model_admin):
    #     lista_de_estab = []
    #     queryset = Base.objects.all()
    #     for estab in queryset:
    #         lista_de_estab.append(
    #             (str(estab.cd_estab), )
    #         )
    #         lista_de_estab.append(('','Todos'))
    #
    #     return lista_de_estab #sorted(lista_de_estab, key=lambda tp: tp[1])
    #
    #
    # def choices(self, cl):
    #     for lookup, title in self.lookup_choices:
    #         yield {
    #             'selected': self.value() == lookup,
    #             'query_string': cl.get_query_string({
    #                 self.parameter_name: lookup,
    #             }, []),
    #             'display': title,
    #         }
    #
    # def queryset(self, request, queryset):
    #     return queryset.filter(cd_estab = self.value())



class PedidoBaseAdmin(admin.ModelAdmin):
    form = PedidoBaseAdminForm

    def related_cliente_grade(self, obj):
        try:
            return '%s' % obj.grade
        except AttributeError:
            return None

    inlines = [ItemInline,]
    #exclude = ('item',)
    verbose_name = ('Pedido')
    list_display = ('dt_saida', 'grade', 'cliente', 'cd_estab', 'ds_transp', ) #'dt_atlz', 'item__nr_nota_fis', 'item__nr_pedido', )
    readonly_fields = ('st_chegada','st_libera')
    fieldsets = (
        (None, {'fields':(
                          # ('dt_atlz', 'usr_atlz'),
                          ('dt_saida','grade' ),('cd_estab', 'cliente',), # 'ds_classe_cli'),
                        ('ds_transp', 'ds_placa','nr_lacre'),
                        ('st_chegada','st_libera'))
                }),
        ('Acompanhamento do Carregamento',{
            'classes':('collapse',),
                'fields':(('dt_hr_chegada','dt_hr_ini_carga','dt_hr_fim_carga', 'dt_hr_liberacao'))
        })
    )
    #readonly_fields = ('cd_estab','nm_ab_cliente','nr_nota_fis','nr_pedido','dt_atlz',)
    list_filter = ('cd_estab',) #'nm_ab_cli') #'[EstabListFilter,]
    search_fields = ['nr_nota_fis','nr_pedido' ,]
admin.site.register(Base, PedidoBaseAdmin)
admin.site.register(Item)