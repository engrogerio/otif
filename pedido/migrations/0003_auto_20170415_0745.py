# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_auto_20170409_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='qt_pallet',
            field=models.IntegerField(default=0, verbose_name=b'Quantidade de Pallets'),
        ),
    ]
