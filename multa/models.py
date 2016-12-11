# -*- encoding: utf-8 -*-

from django.db import models
from sgo.models import OtifModel
from pedido.models import Carregamento, Item
from decimal import *

class MultaItem(OtifModel):

    vl_base_multa = models.DecimalField('Valor base da multa (R$)', null='true', blank='true', max_digits=17,
                                        decimal_places=2)
    vl_multa = models.DecimalField('Valor da multa (R$)', null='true', blank='true', max_digits=17, decimal_places=2)
    item = models.ForeignKey(Item, null='true', blank='true',)

    def save(self):
        try:
            self.vl_multa = self.vl_base_multa*self.item.qt_falta
        except:
            self.vl_multa = 0
        super(MultaItem, self).save()

    def __unicode__(self):
        return ''

class MultaCarregamento(OtifModel):

    vl_fixo = models.DecimalField('Valor fixo da multa (R$)', null='true', blank='true', max_digits=17,
                                  decimal_places=2, )
    vl_base_multa = models.DecimalField('Valor base da multa (R$)', null='true', blank='true', max_digits=17,
                                        decimal_places=2)
    vl_multa = models.DecimalField('Valor da multa (R$)', null='true', blank='true', max_digits=17, decimal_places=2)
    carregamento = models.ForeignKey(Carregamento, null='true', blank='true',)

    def save(self):
        if self.carregamento.id_no_show==Carregamento.SIM:
            self.vl_multa = self.vl_base_multa*Decimal('0.05')+self.vl_fixo
        else:
            self.vl_multa = 0
        super(MultaCarregamento, self).save()

    def __unicode__(self):
        return ''