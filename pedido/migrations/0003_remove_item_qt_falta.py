# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_auto_20170125_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='qt_falta',
        ),
    ]
