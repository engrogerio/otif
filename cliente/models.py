# -*- encoding: utf-8 -*-
from django.db import models
from sgo.models import OtifModel
# Create your models here.

class Cliente(OtifModel):
    nm_ab_cli = models.CharField('Código do cliente', max_length=24, unique='true', )
    ds_classe_cli = models.CharField('Canal do cliente', max_length=30, null='true', blank='true', )
    hr_lim_carga = models.TimeField('Limite de atraso de carregamento (hs)', null='true', blank='true', )
    hr_lim_lib = models.TimeField('Limite de atraso de liberação (hs)', null='true', blank='true', )

    class Meta:
        verbose_name_plural = "Limites por Cliente"

    def __unicode__(self):
        return  self.nm_ab_cli
