# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessunit',
            name='cd_unit',
            field=models.CharField(verbose_name='Código do Estab.', max_length=5),
        ),
        migrations.AlterField(
            model_name='businessunit',
            name='unit',
            field=models.CharField(verbose_name='Nome do Estab.', max_length=100),
        ),
        migrations.AlterField(
            model_name='user_businessunit',
            name='unit',
            field=models.ForeignKey(related_name='unit_business_unit', to='business_unit.BusinessUnit', verbose_name='Cód. Estab.'),
        ),
        migrations.AlterField(
            model_name='user_businessunit',
            name='user',
            field=models.ForeignKey(related_name='user_business_unit', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='user_estabelecimento',
            name='unit',
            field=models.ForeignKey(related_name='unit_estabelecimento', to='business_unit.BusinessUnit', verbose_name='Cód. Estab.'),
        ),
        migrations.AlterField(
            model_name='user_estabelecimento',
            name='user',
            field=models.OneToOneField(related_name='user_estabelecimento', verbose_name='Usuário',  to=settings.AUTH_USER_MODEL ),
        ),
    ]
