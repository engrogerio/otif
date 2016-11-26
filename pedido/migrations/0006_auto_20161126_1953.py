# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_auto_20161126_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='carregamento',
            name='ds_status_cheg',
            field=models.CharField(max_length=15, null=b'true', verbose_name=b'Status de chegada', blank=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='ds_status_lib',
            field=models.CharField(max_length=15, null=b'true', verbose_name=b'Status de libera\xc3\xa7\xc3\xa3o', blank=b'true'),
        ),
    ]
