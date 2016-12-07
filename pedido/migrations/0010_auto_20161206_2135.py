# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0009_auto_20161203_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='dt_saida',
            field=models.DateField(null=b'true', verbose_name=b'Data do Carregamento', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='hr_grade',
            field=models.TimeField(null=b'true', verbose_name=b'Hor\xc3\xa1rio do Carregamento', blank=b'true'),
        ),
    ]
