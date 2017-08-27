# # -*- encoding=utf-8 -*-
#
# from pedido.forms import UpdateDateForm
# from django.views.generic import View
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.utils.decorators import classonlymethod
# from django.contrib import admin
# # from pedido.admin.carregamento_admin import PedidoCarregamentoAdmin
#
#
# class SetChegada(View):
#     Form = UpdateDateForm
#     template_name = 'pedido/add_date.html'
#
#     short_description = 'Sinalizar chegada do caminhão'
#
#     action_name = 'admin_action'
#
#     def actionOnEntry(self, entry, form):
#         # Get the data from the form
#         date = form.cleaned_data['data']
#         # Do the updates to the entry
#         entry.set_chegada(date)
#         # Add change on log
#         # PedidoCarregamentoAdmin.add_log_carregamento()
#         # Save the entry
#         entry.save()
#
#     def post(self, request, modeladmin, queryset):
#         form = None
#
#         if 'apply' in request.POST:
#
#             form = self.Form(request.POST)
#
#             if form.is_valid():
#
#                 count = 0
#                 for c in queryset:
#                     self.actionOnEntry(c, form)
#                     count += 1
#
#                 plural = False
#                 if count != 1:
#                     plural = True
#
#                 modeladmin.message_user(request, "%i %s como Caminhão na planta" % (
#                 count, "carregamento marcado" if not plural else "carregamentos marcados"))
#                 return HttpResponseRedirect(request.get_full_path())
#
#         if not form:
#             form = self.Form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
#
#         context = {
#             'queryset': queryset,
#             'form': form,
#             'action_name': self.action_name,
#         }
#
#         return render(request, self.template_name, context)
#
#
#     @classonlymethod
#     def as_admin_view(cls, **initkwargs):
#         view = cls.as_view(**initkwargs)
#
#         def admin_view(modeladmin, request, *args, **kwargs):
#             return view(request, modeladmin, *args, **kwargs)
#
#         admin_view.short_description = cls.short_description
#         admin_view.__name__ = cls.action_name
#
#         return admin_view
#
#
#
# class SetInicio(View):
#     Form = UpdateDateForm
#     template_name = 'pedido/add_date.html'
#
#     short_description = 'Sinalizar início do Carregamento'
#
#     action_name = 'admin_action'
#
#     def actionOnEntry(self, entry, form):
#         # Get the data from the form
#         date = form.cleaned_data['data']
#         # Do the updates to the entry
#         entry.set_inicio(date)
#         # Add change on log
#         # PedidoCarregamentoAdmin.add_log_carregamento()
#         # Save the entry
#         entry.save()
#
#     def post(self, request, modeladmin, queryset):
#         form = None
#
#         if 'apply' in request.POST:
#
#             form = self.Form(request.POST)
#
#             if form.is_valid():
#
#                 count = 0
#                 for entry in queryset:
#                     self.actionOnEntry(entry, form)
#                     count += 1
#
#                 plural = False
#                 if count != 1:
#                     plural = True
#
#                 modeladmin.message_user(request, "%i %s como carregamento iniciado." % (
#                 count, "carregamento marcado" if not plural else "carregamentos marcados"))
#                 return HttpResponseRedirect(request.get_full_path())
#
#         if not form:
#             form = self.Form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
#
#         context = {
#             'queryset': queryset,
#             'form': form,
#             'action_name': self.action_name,
#         }
#
#         return render(request, self.template_name, context)
#
#
#     @classonlymethod
#     def as_admin_view(cls, **initkwargs):
#         view = cls.as_view(**initkwargs)
#
#         def admin_view(modeladmin, request, *args, **kwargs):
#             return view(request, modeladmin, *args, **kwargs)
#
#         admin_view.short_description = cls.short_description
#         admin_view.__name__ = cls.action_name
#
#         return admin_view
