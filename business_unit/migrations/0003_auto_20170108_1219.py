# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0002_businessunit_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessunit',
            name='users',
        ),
        migrations.AddField(
            model_name='user_businessunit',
            name='unit',
            field=models.ForeignKey(related_name='unit_business_unit', default=1, verbose_name=b'Unidade', to='business_unit.BusinessUnit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_businessunit',
            name='user',
            field=models.OneToOneField(related_name='unit_business_user', verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL),
        ),
    ]
