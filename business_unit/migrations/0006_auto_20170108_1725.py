# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0005_auto_20170108_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit_businessunit',
            name='user',
            field=models.ForeignKey(related_name='user_business_unit', verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL),
        ),
    ]
