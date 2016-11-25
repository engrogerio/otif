# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hr_grade', models.IntegerField(blank=b'true', null=b'true', verbose_name=b'Hor\xc3\xa1rio', choices=[(0, b'0:00'), (1, b'1:00'), (2, b'2:00'), (3, b'3:00'), (4, b'4:00'), (5, b'5:00'), (6, b'6:00'), (7, b'7:00'), (8, b'8:00'), (9, b'9:00'), (10, b'10:00'), (11, b'11:00'), (12, b'12:00'), (13, b'13:00'), (14, b'14:00'), (15, b'15:00'), (16, b'16:00'), (17, b'17:00'), (18, b'18:00'), (19, b'19:00'), (20, b'20:00'), (21, b'21:00'), (22, b'22:00'), (23, b'23:00')])),
                ('dt_semana', models.IntegerField(blank=b'true', null=b'true', verbose_name=b'Dia da semana', choices=[(0, b'Segunda-feira'), (1, b'Ter\xc3\xa7a-feira'), (2, b'Quarta-feira'), (3, b'Quinta-feira'), (4, b'Sexta-feira'), (5, b'S\xc3\xa1bado'), (6, b'Domingo')])),
                ('cliente', models.ForeignKey(db_column=b'nm_ab_cli', to_field=b'nm_ab_cli', blank=b'true', to='cliente.Cliente', null=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
