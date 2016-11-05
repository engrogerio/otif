# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from business_unit.models import User_BusinessUnit
from business_unit.models import BusinessUnit
from django import forms


# Define an inline admin descriptor for BusinessUnit model
# which acts a bit like a singleton
class User_BusinessUnitInline(admin.StackedInline):
    model = User_BusinessUnit
    can_delete = False
    verbose_name_plural = 'Unidade de Negócios do Usuário'

# Define a new User admin
class MyUserAdmin(UserAdmin):
    inlines = (User_BusinessUnitInline, )

    def __init__(self, *args, **kwargs):
        super(MyUserAdmin,self).__init__(*args, **kwargs)
        MyUserAdmin.list_display =['username','email','first_name','last_name','user_business_unit']
        #MyUserAdmin.list_filter+=('user_business_unit',)
#________________________________________________________________________________________

class UserBusinessUnitAdminForm(forms.ModelForm):
    class Meta:
        model = User_BusinessUnit
        fields = "__all__"

class UserBusinessUnitAdmin(admin.ModelAdmin):
    form = UserBusinessUnitAdminForm
    fieldsets = (
        (None, {
            'fields':(('business_unit'),('user',),),
        }),
    )
    list_display = ('user','business_unit',)
#_________________________________________________________________________________________


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

admin.site.register(BusinessUnit)
admin.site.register(User_BusinessUnit, UserBusinessUnitAdmin)