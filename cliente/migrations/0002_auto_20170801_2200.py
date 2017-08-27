# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ds_classe_cli',
            field=models.CharField(blank='true', verbose_name='Canal do cliente',  max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='hr_lim_carga',
            field=models.TimeField(blank='true', verbose_name='Limite de atraso de carregamento (hs)'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='hr_lim_lib',
            field=models.TimeField(blank='true', verbose_name='Limite de atraso de liberação (hs)'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nm_ab_cli',
            field=models.CharField(max_length=24, verbose_name='Código do cliente', unique='true'),
        ),
    ]
