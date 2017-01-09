# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_unit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessunit',
            name='users',
            field=models.ForeignKey(related_name='business_unit_users', default=1, verbose_name=b'Usu\xc3\xa1rios', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
