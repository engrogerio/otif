
#_*_ coding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import User


class BusinessUnit(models.Model):
    cd_unit = models.CharField('Código do Estab.', max_length=5)
    unit = models.CharField('Nome do Estab.', max_length=100,)

    def __unicode__(self):
        return self.cd_unit or u''

    class Meta():
        verbose_name = u'Estabelecimento'
        verbose_name_plural = u'Estabelecimentos'
        default_permissions = ('add', 'change', 'delete', 'view')

class BusinessUnitSpecificModel(models.Model):
    #All business unit specific models should extend this class instead of
    #models.Model directly.
    business_unit=models.ForeignKey(BusinessUnit, verbose_name='Cód. Estab.',
        null='true', blank='true',)

    class Meta:
        abstract = True

class User_BusinessUnit(models.Model):
    """
    Business units that an specific user is able to see. This is defined on the
    form for User. One user may have many BusinessUnits
    """
    unit = models.ForeignKey(BusinessUnit, verbose_name='Cód. Estab.',
        related_name='unit_business_unit')
    user = models.ForeignKey(User, verbose_name='Usuário',
        related_name='user_business_unit')

    def __unicode__(self):
        return self.unit.unit or u''

    class Meta():
        verbose_name = u'Estabs. que o usuário pode acessar'
        verbose_name_plural = u'Estabs. que o usuário pode acessar'

class User_Estabelecimento(BusinessUnitSpecificModel):
    """
    Business unit that an specific user is currently on. This is defined on
    the form for User. One user has only one User_Estabelecimento.
    """
    user = models.OneToOneField(User, verbose_name='Usuário',
        null='true', blank='true',) #related_name='user_business_unit')

    def __unicode__(self):
        return self.business_unit.unit or u''

    class Meta():
        verbose_name = u'Estab. do Usuário'
        verbose_name_plural = u'Estab. do Usuário'
