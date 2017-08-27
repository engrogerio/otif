# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_auto_20170801_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='business_unit',
            field=models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='dt_semana',
            field=models.IntegerField(default=0, verbose_name=b'Dia da semana', choices=[(0, b'Segunda-feira'), (1, b'Ter\xc3\xa7a-feira'), (2, b'Quarta-feira'), (3, b'Quinta-feira'), (4, b'Sexta-feira'), (5, b'S\xc3\xa1bado'), (6, b'Domingo')]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='hr_grade',
            field=models.TimeField(verbose_name=b'Hor\xc3\xa1rio'),
        ),
    ]
