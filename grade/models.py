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

    HR0 =0
    HR1 =1
    HR2 =2
    HR3 =3
    HR4 =4
    HR5 =5
    HR6 =6
    HR7 =7
    HR8 =8
    HR9 =9
    HR10=10
    HR11=11
    HR12=12
    HR13=13
    HR14=14
    HR15=15
    HR16=16
    HR17=17
    HR18=18
    HR19=19
    HR20=20
    HR21=21
    HR22=22
    HR23=23

    HORA_GRADE = (
        (HR0, '0:00'),
        (HR1, '1:00'),
        (HR2, '2:00'),
        (HR3, '3:00'),
        (HR4, '4:00'),
        (HR5, '5:00'),
        (HR6, '6:00'),
        (HR7, '7:00'),
        (HR8, '8:00'),
        (HR9, '9:00'),
        (HR10, '10:00'),
        (HR11, '11:00'),
        (HR12, '12:00'),
        (HR13, '13:00'),
        (HR14, '14:00'),
        (HR15, '15:00'),
        (HR16, '16:00'),
        (HR17, '17:00'),
        (HR18, '18:00'),
        (HR19, '19:00'),
        (HR20, '20:00'),
        (HR21, '21:00'),
        (HR22, '22:00'),
        (HR23, '23:00')
    )

    cliente = models.ForeignKey(Cliente, null='true', blank='true', to_field='nm_ab_cli', db_column='nm_ab_cli')
    hr_grade = models.IntegerField ('Horário', choices = HORA_GRADE, null='true', blank='true', )
    dt_semana = models.IntegerField('Dia da semana',choices = DIA_SEMANA, null='true', blank='true',)

    def get_grade(self,cliente,data):
        data_aux = datetime.datetime.strptime(data, "%d/%m/%Y").date()
        dia_semana = datetime.datetime(data_aux).weekday()

    def __unicode__(self):
        return str(self.hr_grade)
