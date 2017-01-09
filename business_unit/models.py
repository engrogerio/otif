
#_*_ coding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import User


class BusinessUnit(models.Model):
    cd_unit = models.CharField('Código da Unidade', max_length=5)
    unit = models.CharField('Unidade de Negócios', max_length=100,)

    def __unicode__(self):
        return self.unit or u''

    class Meta():
        verbose_name = u'Unidade de Negócios'
        verbose_name_plural = u'Unidades de Negócio'
        default_permissions = ('add', 'change', 'delete', 'view')

class BusinessUnitSpecificModel(models.Model):
    #All business unit specific models should extend this class instead of
    #models.Model directly.
    business_unit=models.ForeignKey(BusinessUnit, null='true', blank='true',)

    class Meta:
        abstract = True

class User_BusinessUnit(models.Model):

    unit = models.ForeignKey(BusinessUnit, verbose_name='Unidade',
        related_name='unit_business_unit')
    user = models.ForeignKey(User, verbose_name='Usuário',
        related_name='user_business_unit')

    def __unicode__(self):
        return self.user.username or u''

    class Meta():
        verbose_name = u'Unidade de Negócio do Usuário'
        verbose_name_plural = u'Unidades de Negócio do Usuário'
