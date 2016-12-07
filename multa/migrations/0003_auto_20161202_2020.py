# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0008_auto_20161202_2020'),
        ('multa', '0002_auto_20161127_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='multacarregamento',
            name='carregamento',
            field=models.ForeignKey(verbose_name=b'Carregamento', blank=b'true', to='pedido.Carregamento', null=b'true'),
        ),
        migrations.AddField(
            model_name='multaitem',
            name='item',
            field=models.ForeignKey(verbose_name=b'Item', blank=b'true', to='pedido.Item', null=b'true'),
        ),
    ]
