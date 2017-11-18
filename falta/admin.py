from django.contrib import admin
from falta.models import Motivo, MotivoAtraso, MotivoDeAlteracaoDaAgenda
# Register your models here.
admin.site.register(Motivo)
admin.site.register(MotivoAtraso)
admin.site.register(MotivoDeAlteracaoDaAgenda)