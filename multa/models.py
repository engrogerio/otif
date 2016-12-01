# -*- encoding: utf-8 -*-

from django.db import models
from sgo.models import OtifModel


class MultaItem(OtifModel):

    vl_base_multa = models.DecimalField('Valor base da multa', null='true', blank='true', max_digits=17,
                                        decimal_places=2)
    vl_multa = models.DecimalField('Valor da multa', null='true', blank='true', max_digits=17, decimal_places=2)


class MultaCarregamento(OtifModel):

    vl_fixo = models.DecimalField('Valor fixo da multa', null='true', blank='true', max_digits=17,
                                  decimal_places=2)
    vl_base_multa = models.DecimalField('Valor base da multa', null='true', blank='true', max_digits=17,
                                        decimal_places=2)
    vl_multa = models.DecimalField('Valor da multa', null='true', blank='true', max_digits=17, decimal_places=2)

class MultaMotivo (OtifModel):

    ds_motivo = models.CharField('Motivo', max_length=200, null='true', blank='true,',)
    ds_obs = models.CharField('Observação', max_length=2000, null='true', blank='true',)