# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multa', '0002_auto_20170801_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multacarregamento',
            name='carregamento',
            field=models.ForeignKey(related_name='carregamento_multa', blank=b'true', to='pedido.Carregamento', null=b'true'),
        ),
        migrations.AlterField(
            model_name='multacarregamento',
            name='vl_multa',
            field=models.DecimalField(null=b'true', verbose_name=b'Valor da multa (R$)', max_digits=17, decimal_places=2, blank=b'true'),
        ),
        migrations.AlterField(
            model_name='multaitem',
            name='item',
            field=models.ForeignKey(related_name='item_multa', blank=b'true', to='pedido.Item', null=b'true'),
        ),
        migrations.AlterField(
            model_name='multaitem',
            name='vl_multa',
            field=models.DecimalField(null=b'true', verbose_name=b'Valor da multa (R$)', max_digits=17, decimal_places=2, blank=b'true'),
        ),
    ]
