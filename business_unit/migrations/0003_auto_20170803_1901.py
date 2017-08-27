# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0002_auto_20170801_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessunit',
            name='cd_unit',
            field=models.CharField(max_length=5, verbose_name=b'C\xc3\xb3digo do Estab.'),
        ),
        migrations.AlterField(
            model_name='user_businessunit',
            name='unit',
            field=models.ForeignKey(related_name='unit_business_unit', verbose_name=b'C\xc3\xb3d. Estab.', to='business_unit.BusinessUnit'),
        ),
        migrations.AlterField(
            model_name='user_businessunit',
            name='user',
            field=models.ForeignKey(related_name='user_business_unit', verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_estabelecimento',
            name='unit',
            field=models.ForeignKey(related_name='unit_estabelecimento', verbose_name=b'C\xc3\xb3d. Estab.', to='business_unit.BusinessUnit'),
        ),
        migrations.AlterField(
            model_name='user_estabelecimento',
            name='user',
            field=models.OneToOneField(related_name='user_estabelecimento', null=b'true', blank=b'true', to=settings.AUTH_USER_MODEL, verbose_name=b'Usu\xc3\xa1rio'),
        ),
    ]
