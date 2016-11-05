# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_auto_20161105_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='base',
        ),
    ]
