# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carregamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vl_fixo', models.DecimalField(null=b'true', verbose_name=b'Valor fixo da multa', max_digits=17, decimal_places=2, blank=b'true')),
                ('vl_base_multa', models.DecimalField(null=b'true', verbose_name=b'Valor base da multa', max_digits=17, decimal_places=2, blank=b'true')),
                ('vl_multa', models.DecimalField(null=b'true', verbose_name=b'Valor da multa', max_digits=17, decimal_places=2, blank=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vl_base_multa', models.DecimalField(null=b'true', verbose_name=b'Valor base da multa', max_digits=17, decimal_places=2, blank=b'true')),
                ('vl_multa', models.DecimalField(null=b'true', verbose_name=b'Valor da multa', max_digits=17, decimal_places=2, blank=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
