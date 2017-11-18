# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta', '0006_auto_20171109_1853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='motivo',
            options={'verbose_name_plural': 'Motivos de falta'},
        ),
    ]
