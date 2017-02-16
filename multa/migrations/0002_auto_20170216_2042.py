# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multacarregamento',
            name='vl_base_multa',
        ),
        migrations.RemoveField(
            model_name='multacarregamento',
            name='vl_fixo',
        ),
        migrations.RemoveField(
            model_name='multaitem',
            name='vl_base_multa',
        ),
    ]
