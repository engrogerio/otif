# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multa', '0004_auto_20161203_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multacarregamento',
            name='carregamento',
            field=models.ForeignKey(blank=b'true', to='pedido.Carregamento', null=b'true'),
        ),
        migrations.AlterField(
            model_name='multaitem',
            name='item',
            field=models.ForeignKey(blank=b'true', to='pedido.Item', null=b'true'),
        ),
    ]
