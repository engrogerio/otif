# -*- encoding: utf-8 -*-
from django.contrib import admin
from grade.models import Grade
from sgo.admin import SgoModelAdmin
from django import forms



class GradeInline(admin.TabularInline):
    model = Grade
    extra = 0
    fields = ['get_grade','hr_grade']


class GradeAdminForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'


class GradeAdmin(SgoModelAdmin):
    def queryset(self, request):
        qs = super(GradeAdmin, self).queryset(request)
        self.request = request
        return qs

    form = GradeAdminForm
    verbose_name = ("Grade")
    list_display = ('business_unit','cliente', 'dt_semana', 'hr_grade',)
    ordering = ('hr_grade',)
    list_filter = ('cliente', 'dt_semana')

# Register your models here.

admin.site.register(Grade, GradeAdmin)
