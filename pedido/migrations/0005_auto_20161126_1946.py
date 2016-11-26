# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_auto_20161126_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carregamento',
            name='ds_status_cheg',
        ),
        migrations.RemoveField(
            model_name='carregamento',
            name='ds_status_lib',
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_carrega',
            field=models.IntegerField(default=0, null=b'true', verbose_name=b'Status', blank=b'true', choices=[(0, b'Carregamento programado'), (1, b'Caminh\xc3\xa3o na planta'), (2, b'Carregamento iniciado'), (3, b'Carregamento finalizado'), (4, b'Caminh\xc3\xa3o liberado')]),
        ),
    ]
