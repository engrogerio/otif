# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='base',
            name='dt_atlz',
        ),
        migrations.RemoveField(
            model_name='base',
            name='usr_atlz',
        ),
        migrations.RemoveField(
            model_name='item',
            name='dt_atlz',
        ),
        migrations.RemoveField(
            model_name='item',
            name='usr_atlz',
        ),
    ]
