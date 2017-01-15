# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0010_auto_20170111_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_estabelecimento',
            name='user',
            field=models.OneToOneField(null=b'true', blank=b'true', to=settings.AUTH_USER_MODEL, verbose_name=b'Usu\xc3\xa1rio'),
        ),
    ]
