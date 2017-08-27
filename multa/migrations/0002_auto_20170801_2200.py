# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multacarregamento',
            name='carregamento',
            field=models.ForeignKey(related_name='carregamento_multa', to='pedido.Carregamento', blank='true'),
        ),
        migrations.AlterField(
            model_name='multacarregamento',
            name='vl_multa',
            field=models.DecimalField(max_digits=17, blank='true', verbose_name='Valor da multa (R$)', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='multaitem',
            name='item',
            field=models.ForeignKey(related_name='item_multa',  to='pedido.Item', blank='true'),
        ),
        migrations.AlterField(
            model_name='multaitem',
            name='vl_multa',
            field=models.DecimalField(max_digits=17, blank='true', verbose_name='Valor da multa (R$)', decimal_places=2),
        ),
    ]
