# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='is_disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
