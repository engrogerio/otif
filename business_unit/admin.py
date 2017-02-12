# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from business_unit.models import User_BusinessUnit
from business_unit.models import User_Estabelecimento
from django import forms


# Define an inline admin descriptor for BusinessUnit model
# which acts a bit like a singleton
class User_BusinessUnitInline(admin.StackedInline):
    model = User_BusinessUnit
    extra = 0
    can_delete = True
    verbose_name_plural = 'Estabelecimentos visíveis'


class User_EstablecimentoInline(admin.StackedInline):
    model = User_Estabelecimento
    extra = 0
    can_delete = True
    verbose_name_plural = 'Estabelecimentos do Usuário'


# Define a new User admin
class MyUserAdmin(UserAdmin):
    inlines = [User_EstablecimentoInline, User_BusinessUnitInline ]

    def __init__(self, *args, **kwargs):
        super(MyUserAdmin,self).__init__(*args, **kwargs)
        MyUserAdmin.list_display =['username','email','first_name','last_name',]
            # 'user_business_unit']
        # MyUserAdmin.list_filter+=('user_business_unit',)


# Define a new User admin
class MyEstabelecimentoUserAdmin(UserAdmin):
    inlines = [User_EstablecimentoInline, ]

    def __init__(self, *args, **kwargs):
        super(MyEstabelecimentoUserAdmin,self).__init__(*args, **kwargs)
        MyEstabelecimentoUserAdmin.list_display =['username','email','first_name','last_name',]
            # 'user_business_unit']
        # MyUserAdmin.list_filter+=('user_business_unit',)


class UserBusinessUnitAdminForm(forms.ModelForm):
    class Meta:
        model = User_BusinessUnit
        fields = "__all__"


class UserBusinessUnitAdmin(admin.ModelAdmin):
    form = UserBusinessUnitAdminForm
    fieldsets = (
        (None, {
            'fields':(('unit','user',),),
        }),
    )
    list_display = ('user','unit')


class User_EstabelecimentoAdminForm(forms.ModelForm):
    class Meta:
        model = User_Estabelecimento
        fields = "__all__"


class User_EstabelecimentoAdmin(admin.ModelAdmin):
    form = User_EstabelecimentoAdminForm
    fieldsets = (
        (None, {
            'fields':(('user','business_unit',),),
        }),
    )
    list_display = ('user','business_unit')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
# admin.site.register(BusinessUnit)
