# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_remove_item_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='item',
            field=models.ManyToManyField(to='pedido.Item', null=b'true', blank=b'true'),
        ),
    ]
