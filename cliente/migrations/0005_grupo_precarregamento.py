# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20171018_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nm_grupo', models.IntegerField(null=b'true', verbose_name=b'C\xc3\xb3digo do Grupo', blank=b'true')),
                ('cliente', models.ManyToManyField(to='cliente.Cliente', null=b'true', blank=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreCarregamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.ManyToManyField(to='cliente.Grupo', null=b'true', blank=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
