# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='ds_ord_compra',
        ),
        migrations.RemoveField(
            model_name='item',
            name='nr_nota_fis',
        ),
        migrations.RemoveField(
            model_name='item',
            name='nr_pedido',
        ),
        migrations.AddField(
            model_name='carregamento',
            name='ds_ord_compra',
            field=models.CharField(max_length=15, null=b'true', verbose_name=b'Ordem de compra', blank=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='nr_pedido',
            field=models.CharField(max_length=24, null=b'true', verbose_name=b'Pedido do cliente', blank=b'true'),
        ),
    ]
