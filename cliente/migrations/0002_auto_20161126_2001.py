# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='hr_lim_carga',
            field=models.TimeField(max_length=5, null=b'true', verbose_name=b'Limite de atraso de carregamento (hs)', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='hr_lim_lib',
            field=models.TimeField(max_length=5, null=b'true', verbose_name=b'Limite de atraso de libera\xc3\xa7\xc3\xa3o (hs)', blank=b'true'),
        ),
    ]
