# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='dt_atlz',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='usr_atlz',
        ),
    ]
