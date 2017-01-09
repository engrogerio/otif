# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_unit', '0004_auto_20170108_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit_BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.ForeignKey(related_name='unit_business_unit', verbose_name=b'Unidade', to='business_unit.BusinessUnit')),
                ('user', models.OneToOneField(related_name='user_business_unit', verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Unidade de Neg\xf3cio do Usu\xe1rio',
                'verbose_name_plural': 'Unidades de Neg\xf3cio do Usu\xe1rio',
            },
        ),
        migrations.RemoveField(
            model_name='user_businessunit',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='user_businessunit',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_BusinessUnit',
        ),
    ]
