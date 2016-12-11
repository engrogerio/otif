# -*- encoding: utf-8 -*-
from django.contrib import admin
from django import forms
from cliente.models import Cliente
# Register your models here.

class ClienteAdminForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class ClienteAdmin(admin.ModelAdmin):
    form = ClienteAdminForm

    #inlines = [GradeInline,]
    #exclude = ('item',)
    verbose_name = ("Cliente")
    list_display = ('nm_ab_cli', 'hr_lim_carga','hr_lim_lib', 'ds_classe_cli', )
    readonly_fields = ()
    fieldsets = (
        (None, {'fields':(
                          (('nm_ab_cli','ds_classe_cli'),('hr_lim_carga','hr_lim_lib',)))
                }),

    )
    list_filter = ('nm_ab_cli',)
    search_fields = ['nm_ab_cli',]


admin.site.register(Cliente, ClienteAdmin)