# -*- coding=utf-8 -*-
from django.db import models
from sgo.models import OtifModel

# Create your models here.
class Motivo (OtifModel):
    class Meta:
        verbose_name_plural = "Motivos de falta"
    id_motivo = models.CharField('Código do Motivo', max_length=10, null='true', blank='true',)
    ds_motivo = models.CharField('Motivo', max_length=200, null='true', blank='true',)

    def __unicode__(self):
        return '' or ''.join([self.id_motivo, ' - ', self.ds_motivo])


class MotivoDeAlteracaoDaAgenda (OtifModel):
    class Meta:
        verbose_name_plural = "Motivos de alteração da agenda"
        
    SIM=1
    NAO=2
    IMPACTA_OTIF=(
        (SIM,'S'),
        (NAO,'N')
    )
    cd_motivo = models.CharField('Código do Motivo', max_length=10, null='true', blank='true')
    ds_motivo = models.CharField('Descrição do Motivo', max_length=200, null='true', blank='true')
    id_impacta = models.IntegerField('Impacta para OTIF', choices=IMPACTA_OTIF, null='true', blank='true')

    def __unicode__(self):
        return '' or ''.join([self.cd_motivo, ' - ', self.ds_motivo])


class MotivoAtraso (OtifModel):
    class Meta:
        verbose_name_plural = "Motivos de atraso de carregamento"
        
    SIM=1
    NAO=2
    IMPACTA_OTIF=(
        (SIM,'S'),
        (NAO,'N')
    )
    cd_motivo = models.CharField('Código do Motivo', max_length=10, null='true', blank='true')
    ds_motivo = models.CharField('Descrição do Motivo', max_length=200, null='true', blank='true')
    id_impacta = models.IntegerField('Impacta para OTIF', choices=IMPACTA_OTIF, null='true', blank='true')

    def __unicode__(self):
        return '' or ''.join([self.cd_motivo, ' - ', self.ds_motivo])