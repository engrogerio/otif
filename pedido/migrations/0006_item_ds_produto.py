# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_auto_20170111_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ds_produto',
            field=models.CharField(max_length=200, null=b'true', verbose_name=b'Descri\xc3\xa7\xc3\xa3o do produto', blank=b'true'),
        ),
    ]
