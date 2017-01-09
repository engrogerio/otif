# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='qt_pallet',
        ),
        migrations.AddField(
            model_name='carregamento',
            name='qt_pallet',
            field=models.IntegerField(null=b'true', verbose_name=b'Quantidade de Pallets', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ds_ord_compra',
            field=models.CharField(max_length=15, null=b'true', verbose_name=b'Ordem de compra', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='nr_nota_fis',
            field=models.CharField(max_length=32, null=b'true', verbose_name=b'Nota fiscal', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='nr_pedido',
            field=models.CharField(max_length=24, null=b'true', verbose_name=b'Pedido do cliente', blank=b'true'),
        ),
    ]
