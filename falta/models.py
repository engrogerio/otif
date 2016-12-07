# -*- coding=utf-8 -*-
from django.db import models
from sgo.models import OtifModel

# Create your models here.
class Motivo (OtifModel):
    id_motivo = models.CharField('Código do Motivo', max_length=10, null='true', blank='true',)
    ds_motivo = models.CharField('Motivo', max_length=200, null='true', blank='true',)

    def __unicode__(self):
        return '' or ''.join([self.id_motivo, ' - ', self.ds_motivo])