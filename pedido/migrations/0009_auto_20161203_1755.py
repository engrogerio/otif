# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0008_auto_20161202_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carregamento',
            name='grade',
        ),
        migrations.AddField(
            model_name='carregamento',
            name='hr_grade',
            field=models.TimeField(null=b'true', verbose_name=b'Hora da grade do cliente', blank=b'true'),
        ),
    ]
