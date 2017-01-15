# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0007_auto_20170108_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessunit',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'verbose_name': 'Estabelecimento', 'verbose_name_plural': 'Estabelecimentos'},
        ),
        migrations.AlterModelOptions(
            name='user_businessunit',
            options={'verbose_name': 'Estabelecimento do Usu\xe1rio', 'verbose_name_plural': 'Estabelecimentos do Usu\xe1rio'},
        ),
        migrations.AlterField(
            model_name='businessunit',
            name='cd_unit',
            field=models.CharField(max_length=5, verbose_name=b'C\xc3\xb3digo do Estab.'),
        ),
        migrations.AlterField(
            model_name='businessunit',
            name='unit',
            field=models.CharField(max_length=100, verbose_name=b'Nome do Estab.'),
        ),
        migrations.AlterField(
            model_name='user_businessunit',
            name='unit',
            field=models.ForeignKey(related_name='unit_business_unit', verbose_name=b'Estabelecimento', to='business_unit.BusinessUnit'),
        ),
    ]
