# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_remove_item_qt_falta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='qt_carregada',
            field=models.IntegerField(default=0, verbose_name=b'Quantidade carregada'),
        ),
        migrations.AlterField(
            model_name='item',
            name='qt_embalagem',
            field=models.IntegerField(default=0, verbose_name=b'Quantidade de embalagens'),
        ),
    ]
