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

    cliente = models.ForeignKey(Cliente, to_field='nm_ab_cli', db_column='nm_ab_cli')
    hr_grade = models.TimeField ('Horário', )
    dt_semana = models.IntegerField('Dia da semana',choices = DIA_SEMANA, default= SEG)

    def cria_grades_para_cliente(self,cliente):
        for semana in range(0,7):
            for hora in range(0,24):
                grade=Grade.objects.create(cliente=cliente, hr_grade=hora, dt_semana=semana, is_disponivel=True)
                grade.save()

    def __unicode__(self):
        return self.hr_grade.__str__()
