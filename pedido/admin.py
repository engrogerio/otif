# -*- encoding: utf-8 -*-

from django.contrib import admin
from pedido.models import Base, Item
from django import forms

# Register your models here.

class BaseAdminForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = "__all__"

class BaseAdmin(admin.ModelAdmin):
    form = BaseAdminForm
    filter_horizontal = ('item', )


    verbose_name = ("Pedido")
    list_display = ('dt_atlz', 'cd_estab', 'nm_ab_cliente', 'nr_nota_fis', 'nr_pedido', )
    fieldsets = (
        (None, {'fields':(('dt_atlz', 'cd_estab'),('nm_ab_cliente', 'nr_nota_fis', 'nr_pedido'),
                ('ds_ord_compra','nr_lacre'),('ds_transp', 'ds_placa'))
                }),
        ('Selecione os ítems para a expedição', {
            'fields':('item',)
        }),
        ('Dados do Pedido',{
            #'classes':('collapse',),
                'fields':(('dt_hr_chegada','dt_hr_ini_carga','dt_hr_fim_carga', 'dt_hr_liberacao'))


        })
    )

admin.site.register(Base, BaseAdmin)
admin.site.register(Item)