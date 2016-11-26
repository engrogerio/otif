# -*- encoding: utf-8 -*-

from django.contrib import admin
from pedido.models import Carregamento, Item
from grade.models import Grade
from cliente.models import Cliente
from django import forms
from django.db.models import Func


# Register your models here.

class PedidoCarregamentoAdminForm(forms.ModelForm):
    class Meta:
        model = Carregamento
        fields = "__all__"

    def __init__(self, *args, **kwds):
        super(PedidoCarregamentoAdminForm, self).__init__(*args, **kwds)
        #cli=self.instance.cliente
        if self.instance.grade:
            grade_queryset = Grade.objects.order_by('hr_grade')
        try:
            self.fields['grade'].queryset = grade_queryset
        except:
            pass

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    fields = ['nr_nota_fis', 'ds_ord_compra', 'cd_produto','un_embalagem','qt_embalagem','qt_pilha','qt_falta', 'qt_carregada', 'qt_pallet', 'adicionar_multa']
    readonly_fields = ['nr_nota_fis','cd_produto','un_embalagem','qt_embalagem','qt_pilha', 'adicionar_multa', 'ds_ord_compra']

    def adicionar_multa(self, obj):
        return '<a href="/pedido/item/'+str(obj.id)+'/">Ver Ítem</a>'

    adicionar_multa.allow_tags = True


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



class PedidoCarregamentoAdmin(admin.ModelAdmin):
    form = PedidoCarregamentoAdminForm

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

    def related_cliente_grade(self, obj):
        try:
            return '%s' % obj.grade
        except AttributeError:
            return None

    inlines = [ItemInline,]
    #exclude = ('item',)
    verbose_name = ('Pedido')
    list_display = ('nr_nota_fis','dt_saida', 'grade', 'cliente', 'cd_estab', 'ds_transp','ds_status_carrega' )
    readonly_fields = ('ds_status_cheg', 'ds_status_lib', 'cliente', 'ds_status_carrega', 'cd_estab', 'ds_transp', )
    fieldsets = (
        (None, {'fields':(
                          # ('dt_atlz', 'usr_atlz'),
                          ('cd_estab','cliente','dt_saida','grade' ),
                        ('ds_transp', 'ds_placa','nr_lacre'),
                        ('ds_status_carrega','ds_status_cheg','ds_status_lib'))
                }),
        ('Acompanhamento do Carregamento',{
            'classes':('collapse',),
                'fields':(('dt_hr_chegada','dt_hr_ini_carga','dt_hr_fim_carga', 'dt_hr_liberacao'))
        })
    )
    #readonly_fields = ('cd_estab','nm_ab_cliente','nr_nota_fis','nr_pedido','dt_atlz',)
    list_filter = ('cd_estab','ds_status_carrega',) #'nm_ab_cli') #'[EstabListFilter,]
    search_fields = ['nr_nota_fis','cliente__nm_ab_cli' ,]
admin.site.register(Carregamento, PedidoCarregamentoAdmin)
admin.site.register(Item)