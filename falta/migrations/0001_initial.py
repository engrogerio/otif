# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_motivo', models.CharField(max_length=10, null=b'true', verbose_name=b'C\xc3\xb3digo do Motivo', blank=b'true')),
                ('ds_motivo', models.CharField(max_length=200, null=b'true', verbose_name=b'Motivo', blank=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
