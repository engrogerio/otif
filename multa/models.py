# -*- encoding: utf-8 -*-

from django.db import models
from sgo.models import OtifModel
from pedido.models import Carregamento, Item

class MultaItem(OtifModel):

    vl_base_multa = models.DecimalField('Valor base da multa', null='true', blank='true', max_digits=17,
                                        decimal_places=2)
    vl_multa = models.DecimalField('Valor da multa', null='true', blank='true', max_digits=17, decimal_places=2)
    item = models.ForeignKey(Item, null='true', blank='true',)

class MultaCarregamento(OtifModel):

    vl_fixo = models.DecimalField('Valor fixo da multa', null='true', blank='true', max_digits=17,
                                  decimal_places=2)
    vl_base_multa = models.DecimalField('Valor base da multa', null='true', blank='true', max_digits=17,
                                        decimal_places=2)
    vl_multa = models.DecimalField('Valor da multa', null='true', blank='true', max_digits=17, decimal_places=2)
    carregamento = models.ForeignKey(Carregamento, null='true', blank='true',)