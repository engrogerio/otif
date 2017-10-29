# -*- encoding: utf-8 -*-
from django.contrib import admin
from django import forms
from cliente.models import Cliente, Grupo, PreCarregamento
from sgo.admin import SgoModelAdmin

# Register your models here.

class LimitePorClienteAdminForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nm_ab_cli', 'hr_lim_carga', 'hr_lim_lib',)


class LimitePorClienteAdmin(SgoModelAdmin):
    form = LimitePorClienteAdminForm

    #inlines = [GradeInline,]
    #exclude = ('item',)
    verbose_name = ("Limites Atraso Cliente")
    list_display = ( 'nm_ab_cli', 'hr_lim_carga', 'hr_lim_lib', ) #'cliente_limite', )
    # readonly_fields = ('nm_ab_cli',)
    fieldsets = (
        (None, {'fields':(
                          (('nm_ab_cli', ),('hr_lim_carga', 'hr_lim_lib',)))
                }),
    )
    #list_filter = ('nm_ab_cli',)
    search_fields = ['nm_ab_cli', ]

class GrupoAdmin(SgoModelAdmin):
    filter_horizontal = ('cliente',)

class PreCarregamentoAdmin(SgoModelAdmin):
    filter_horizontal = ('grupo',)

admin.site.register(Cliente, LimitePorClienteAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(PreCarregamento, PreCarregamentoAdmin)