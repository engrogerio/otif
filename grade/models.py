# -*- encoding: utf-8 -*-
from django.db import models
from sgo.models import OtifModel
from cliente.models import Cliente
import datetime
# Create your models here.



class Grade(OtifModel):
    SEG = 0
    TER = 1
    QUA = 2
    QUI = 3
    SEX = 4
    SAB = 5
    DOM = 6

    DIA_SEMANA = (
        (SEG, 'Segunda-feira'),
        (TER, 'Terça-feira'),
        (QUA, 'Quarta-feira'),
        (QUI, 'Quinta-feira'),
        (SEX, 'Sexta-feira'),
        (SAB, 'Sábado'),
        (DOM, 'Domingo'),
    )

    cliente = models.ForeignKey(Cliente, null='true', blank='true', to_field='nm_ab_cli', db_column='nm_ab_cli')
    hr_grade = models.TimeField('Horário', null='true', blank='true',)
    dt_semana = models.IntegerField('Dia da semana',choices = DIA_SEMANA, null='true', blank='true',)

    def get_grade(self,cliente,data):
        data_aux = datetime.datetime.strptime(data, "%d/%m/%Y").date()
        dia_semana = datetime.datetime(data_aux).weekday()

    def __unicode__(self):
        return str(self.hr_grade)
