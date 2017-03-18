# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nm_ab_cli', models.CharField(unique=b'true', max_length=24, verbose_name=b'C\xc3\xb3digo do cliente')),
                ('ds_classe_cli', models.CharField(max_length=30, null=b'true', verbose_name=b'Classifica\xc3\xa7\xc3\xa3o do cliente', blank=b'true')),
                ('hr_lim_carga', models.TimeField(null=b'true', verbose_name=b'Limite de atraso de carregamento (hs)', blank=b'true')),
                ('hr_lim_lib', models.TimeField(null=b'true', verbose_name=b'Limite de atraso de libera\xc3\xa7\xc3\xa3o (hs)', blank=b'true')),
            ],
            options={
                'verbose_name_plural': 'Limites por Cliente',
            },
        ),
    ]
