# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cd_unit', models.CharField(max_length=5, verbose_name=b'C\xc3\xb3digo da Unidade')),
                ('unit', models.CharField(max_length=100, verbose_name=b'Unidade de Neg\xc3\xb3cios')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'verbose_name': 'Unidade de Neg\xf3cios',
                'verbose_name_plural': 'Unidades de Neg\xf3cio',
            },
        ),
        migrations.CreateModel(
            name='User_BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_unit', models.ForeignKey(blank=b'true', to='business_unit.BusinessUnit', null=b'true')),
                ('user', models.OneToOneField(related_name='user_business_unit', verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Unidade de Neg\xf3cio do Usu\xe1rio',
                'verbose_name_plural': 'Unidades de Neg\xf3cio do Usu\xe1rio',
            },
        ),
    ]
