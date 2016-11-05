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



admin.site.register(Base,)
admin.site.register(Item)