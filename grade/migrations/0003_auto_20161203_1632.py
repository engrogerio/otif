# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_grade_is_disponivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='is_disponivel',
        ),
        migrations.AlterField(
            model_name='grade',
            name='hr_grade',
            field=models.TimeField(null=b'true', verbose_name=b'Hor\xc3\xa1rio', blank=b'true'),
        ),
    ]
