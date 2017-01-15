# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_auto_20170110_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carregamento',
            name='cd_estab',
        ),
        migrations.RemoveField(
            model_name='item',
            name='cd_estab',
        ),
    ]
