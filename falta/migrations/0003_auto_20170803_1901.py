# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta', '0002_auto_20170801_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motivo',
            name='ds_motivo',
            field=models.CharField(max_length=200, null=b'true', verbose_name=b'Motivo', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='motivo',
            name='id_motivo',
            field=models.CharField(max_length=10, null=b'true', verbose_name=b'C\xc3\xb3digo do Motivo', blank=b'true'),
        ),
    ]
