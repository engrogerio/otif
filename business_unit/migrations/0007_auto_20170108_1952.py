# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0006_auto_20170108_1725'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Unit_BusinessUnit',
            new_name='User_BusinessUnit',
        ),
    ]
