# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dt_atlz', models.DateTimeField(null=b'true', verbose_name=b'Data atualiza\xc3\xa7\xc3\xa3o', blank=b'true')),
                ('hr_grade', models.TimeField(null=b'true', verbose_name=b'Hor\xc3\xa1rio', blank=b'true')),
                ('dt_semana', models.IntegerField(blank=b'true', null=b'true', verbose_name=b'Dia da semana', choices=[(0, b'Segunda-feira'), (1, b'Ter\xc3\xa7a-feira'), (2, b'Quarta-feira'), (3, b'Quinta-feira'), (4, b'Sexta-feira'), (5, b'S\xc3\xa1bado'), (6, b'Domingo')])),
                ('cliente', models.ForeignKey(db_column=b'nm_ab_cli', to_field=b'nm_ab_cli', blank=b'true', to='cliente.Cliente', null=b'true')),
                ('usr_atlz', models.ForeignKey(blank=b'true', to=settings.AUTH_USER_MODEL, null=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
