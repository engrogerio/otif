# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0003_auto_20170108_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_businessunit',
            name='business_unit',
        ),
        migrations.AlterField(
            model_name='user_businessunit',
            name='user',
            field=models.OneToOneField(related_name='user_business_unit', verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL),
        ),
    ]
