# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motivo',
            name='ds_motivo',
            field=models.CharField(blank='true', verbose_name='Motivo', max_length=200),
        ),
        migrations.AlterField(
            model_name='motivo',
            name='id_motivo',
            field=models.CharField(blank='true', verbose_name='Código do Motivo', max_length=10),
        ),
    ]
