# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta', '0001_initial'),
        ('pedido', '0013_auto_20161210_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id_motivo',
        ),
        migrations.AddField(
            model_name='item',
            name='motivo',
            field=models.ForeignKey(blank=b'true', to='falta.Motivo', null=b'true'),
        ),
    ]
