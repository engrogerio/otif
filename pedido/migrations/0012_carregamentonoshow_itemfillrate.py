# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0011_auto_20161207_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarregamentoNoShow',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pedido.carregamento',),
        ),
        migrations.CreateModel(
            name='ItemFillRate',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pedido.item',),
        ),
    ]
