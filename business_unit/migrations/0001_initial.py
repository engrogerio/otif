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
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cd_unit', models.CharField(max_length=5, verbose_name=b'C\xc3\xb3digo do Estab.')),
                ('unit', models.CharField(max_length=100, verbose_name=b'Nome do Estab.')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'verbose_name': 'Estabelecimento',
                'verbose_name_plural': 'Estabelecimentos',
            },
        ),
        migrations.CreateModel(
            name='User_BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.ForeignKey(related_name='unit_business_unit', verbose_name=b'C\xc3\xb3d. Estab.', to='business_unit.BusinessUnit')),
                ('user', models.ForeignKey(related_name='user_business_unit', verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estabs. que o usu\xe1rio pode acessar',
                'verbose_name_plural': 'Estabs. que o usu\xe1rio pode acessar',
            },
        ),
        migrations.CreateModel(
            name='User_Estabelecimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_unit', models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true')),
                ('user', models.OneToOneField(null=b'true', blank=b'true', to=settings.AUTH_USER_MODEL, verbose_name=b'Usu\xc3\xa1rio')),
            ],
            options={
                'verbose_name': 'Estab. do Usu\xe1rio',
                'verbose_name_plural': 'Estab. do Usu\xe1rio',
            },
        ),
    ]
