# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dt_atlz', models.DateTimeField(null=b'true', verbose_name=b'Data atualiza\xc3\xa7\xc3\xa3o', blank=b'true')),
                ('nm_ab_cli', models.CharField(unique=b'true', max_length=24, verbose_name=b'C\xc3\xb3digo do cliente', db_index=True)),
                ('hr_lim_carga', models.CharField(max_length=5, null=b'true', verbose_name=b'Limite de atraso de carregamento (hs)', blank=b'true')),
                ('hr_lim_lib', models.CharField(max_length=5, null=b'true', verbose_name=b'Limite de atraso de libera\xc3\xa7\xc3\xa3o (hs)', blank=b'true')),
                ('ds_classe_cli', models.CharField(max_length=30, null=b'true', verbose_name=b'Classifica\xc3\xa7\xc3\xa3o do cliente', blank=b'true')),
                ('usr_atlz', models.ForeignKey(blank=b'true', to=settings.AUTH_USER_MODEL, null=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
