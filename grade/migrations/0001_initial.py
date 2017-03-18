# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hr_grade', models.TimeField(verbose_name=b'Hor\xc3\xa1rio')),
                ('dt_semana', models.IntegerField(default=0, verbose_name=b'Dia da semana', choices=[(0, b'Segunda-feira'), (1, b'Ter\xc3\xa7a-feira'), (2, b'Quarta-feira'), (3, b'Quinta-feira'), (4, b'Sexta-feira'), (5, b'S\xc3\xa1bado'), (6, b'Domingo')])),
                ('business_unit', models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true')),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
