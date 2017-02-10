# -*- coding: utf-8 -*-

from django.contrib.contenttypes.models import ContentType
from django.contrib import admin
from django import forms


class SgoTabularInlineAdmin(admin.TabularInline):
    """
    Editable Inlines must extends this class and implement a method: is_readonly that returns False
    Read Only Inlines must extends the Editable Inlines and overwrite is_readonly method to returns True and
    add all fields to declaration readonly_fields = ('field',)
    """
    def has_change_permission(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        saida = False
        if request.user.is_superuser:
            saida = True
        else:
            if request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
                saida = True
            else:
                if request.user.has_perm('%s.change_%s' % (ct.app_label, ct.model)):
                    saida = True
                else:
                    saida = False
        return saida

class SgoModelAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_max_show_all = 5000

    def has_delete_permission(self, request, obj=None):
        #Disable delete
        return False

    def change_view(self, request, object_id, form_url='',extra_context=None):
        ct = ContentType.objects.get_for_model(self.model)
        if not request.user.is_superuser and request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
            extra_context = extra_context or {}
            extra_context['readonly'] = True

        return super(SgoModelAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def has_change_permission(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        saida = False
        if request.user.is_superuser:
            saida = True
        else:
             if request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
                saida = True
             else:
                if request.user.has_perm('%s.change_%s' % (ct.app_label, ct.model)):
                    saida = True
                else:
                    saida = False
        return saida

    def get_readonly_fields(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        if not request.user.is_superuser and request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
            readonly = list(self.readonly_fields) + [el.name for el in self.model._meta.fields]
            return readonly
        else:
            return self.readonly_fields

    def get_formsets_with_inlines(self, request, obj=None):
        """
        Choose whith inline will be hiden based on user being super user or has view permission or not.
        """
        for inline in self.get_inline_instances(request, obj):
            ct = ContentType.objects.get_for_model(inline.model)
            # hide ReadOnly Inline when user has not view permission or when user is super user
            if not request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)) or request.user.is_superuser:
                if inline.is_readonly():
                    continue
                else:
                    yield inline.get_formset(request, obj), inline
                    break
            else:
            # hide Editable Inline when user has view permission
                if not inline.is_readonly():
                    continue
                else:
                    yield inline.get_formset(request, obj), inline
                    break

#Thanks http://www.ibm.com/developerworks/library/os-django-admin/
    """
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'business_unit', None) is None:
            user = User.objects.get(username=request.user)
            obj.business_unit = user.user_business_unit.business_unit
        obj.save()
    """
    def get_queryset(self, request):
        self.user = request.user
        qs = super(SgoModelAdmin, self).get_queryset(request)
        return qs

    def get_form(self, request, obj=None, **kwargs):
        form = super(SgoModelAdmin, self).get_form(request, obj, **kwargs)
        form.user = request.user
        return form
