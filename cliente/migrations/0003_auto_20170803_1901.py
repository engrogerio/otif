# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20170801_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ds_classe_cli',
            field=models.CharField(max_length=30, null=b'true', verbose_name=b'Canal do cliente', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='hr_lim_carga',
            field=models.TimeField(null=b'true', verbose_name=b'Limite de atraso de carregamento (hs)', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='hr_lim_lib',
            field=models.TimeField(null=b'true', verbose_name=b'Limite de atraso de libera\xc3\xa7\xc3\xa3o (hs)', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nm_ab_cli',
            field=models.CharField(unique=b'true', max_length=24, verbose_name=b'C\xc3\xb3digo do cliente'),
        ),
    ]
