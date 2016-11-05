# -*- encoding: utf-8 -*-
from django.db import models
from sgo.models import OtifModel

# Create your models here.
"""
Aplicação: Cadastro

    Modelo:Transportadora
        nm_transportadora       Nome da transportadora

    Modelo: Cliente
        nr_ab_cliente           Código do cliente
        nm_cliente              Nome do cliente
        lim_atraso_carga        Limite de atraso de carregamento (mins)
        lim_atraso_liberacao    Limite de atraso de liberação (mins)
        ds_classe_cliente = models.CharField('Classificação do cliente', max_length=30, null='true', blank='true', )

    Modelo: Grade
        cliente                 relacionamento com cliente
        ds_dia_semana_grade     Dia da semana
        hr_grade                Horario da grade

    Modelo: Produto
        cd_produto = models.CharField('Código do produto', max_length=32, )
        ds_produto = models.CharField('Descrição do produto', max_length=255, null='true', blank='true', )
        un_embalagem = models.CharField('Unidade de embalagem', max_length=3, null='true', blank='true', )
"""

class Cliente(OtifModel):
    nr_ab_cliente = models.CharField('Classificação do cliente', max_length=30, null='true', blank='true', )
    nm_cliente = models.CharField('Nome do cliente', max_length=30, null='true', blank='true', )
    lim_atraso_carga = models.CharField('Limite de atraso de carregamento (mins)', max_length=30, null='true', blank='true', )
    lim_atraso_liberacao = models.CharField('Limite de atraso de liberação (mins)', max_length=30, null='true', blank='true', )
    ds_classe_cliente = models.CharField('Classificação do cliente', max_length=30, null='true', blank='true', )

class Grade(OtifModel):
    cliente = models.ForeignKey(Cliente, null='true', blank='true')
    ds_dia_semana_grade = models.CharField('Dia da Semana', max_length=30, null='true', blank='true',)
    hr_grade = models.TimeField('Horário da Grade', null='true', blank='true',)

class Produto(OtifModel):
    cd_produto = models.CharField('Código do produto', max_length=32, )
    ds_produto = models.CharField('Descrição do produto', max_length=255, null='true', blank='true', )
    un_embalagem = models.CharField('Unidade de embalagem', max_length=3, null='true', blank='true', )

class Transportadora(OtifModel):
    nm_transportadora = models.CharField('Nome da transportadora', max_length=255,)