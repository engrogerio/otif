# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta', '0003_auto_20170803_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivoAlteraAgenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cd_motivo', models.CharField(max_length=10, null=b'true', verbose_name=b'C\xc3\xb3digo do Motivo', blank=b'true')),
                ('ds_motivo', models.CharField(max_length=200, null=b'true', verbose_name=b'Descri\xc3\xa7\xc3\xa3o do Motivo', blank=b'true')),
                ('id_impacta', models.IntegerField(blank=b'true', null=b'true', verbose_name=b'Impacta para OTIF', choices=[(1, b'S'), (2, b'N')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
