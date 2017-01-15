# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_unit', '0008_auto_20170110_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Estabelecimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_unit', models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true')),
                ('user', models.OneToOneField(verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estabelecimento do Usu\xe1rio',
                'verbose_name_plural': 'Estabelecimentos do Usu\xe1rio',
            },
        ),
        migrations.AlterModelOptions(
            name='user_businessunit',
            options={'verbose_name': 'Estabelecimento que o usu\xe1rio pode acessar', 'verbose_name_plural': 'Estabelecimentos que o usu\xe1rio pode acessar'},
        ),
    ]
