# -*- encoding: utf-8 -*-

from django.db import models
from sgo.models import OtifModel
from pedido.models import Carregamento, Item


class MultaItem(OtifModel):

    vl_multa = models.DecimalField('Valor da multa (R$)', null='true', blank='true', max_digits=17, decimal_places=2)
    item = models.ForeignKey(Item, null='true', blank='true', related_name='item_multa')

    def __unicode__(self):
        return ''


class MultaCarregamento(OtifModel):

    vl_multa = models.DecimalField('Valor da multa (R$)', null='true', blank='true', max_digits=17, decimal_places=2)
    carregamento = models.ForeignKey(Carregamento, null='true', blank='true', related_name='carregamento_multa')

    def __unicode__(self):
        return ''
