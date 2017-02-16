# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_estabelecimento',
            name='business_unit',
        ),
        migrations.AddField(
            model_name='user_estabelecimento',
            name='unit',
            field=models.ForeignKey(related_name='unit_estabelecimento', verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true'),
        ),
        migrations.AlterField(
            model_name='user_estabelecimento',
            name='user',
            field=models.OneToOneField(related_name='user_estabelecimento', null=b'true', blank=b'true', to=settings.AUTH_USER_MODEL, verbose_name=b'Usu\xc3\xa1rio'),
        ),
    ]
