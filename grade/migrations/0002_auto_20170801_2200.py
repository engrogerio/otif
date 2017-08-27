# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='business_unit',
            field=models.ForeignKey(verbose_name='Cód. Estab.', to='business_unit.BusinessUnit', blank='true'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='dt_semana',
            field=models.IntegerField(default=0, choices=[(0, 'Segunda-feira'), (1, 'Terça-feira'), (2, 'Quarta-feira'), (3, 'Quinta-feira'), (4, 'Sexta-feira'), (5, 'Sábado'), (6, 'Domingo')], verbose_name='Dia da semana'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='hr_grade',
            field=models.TimeField(verbose_name='Horário'),
        ),
    ]
