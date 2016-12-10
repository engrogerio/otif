# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0012_carregamentonoshow_itemfillrate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarregamentoNoShow',
        ),
        migrations.DeleteModel(
            name='ItemFillRate',
        ),
        migrations.CreateModel(
            name='FillRate',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pedido.item',),
        ),
        migrations.CreateModel(
            name='NoShow',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pedido.carregamento',),
        ),
    ]
