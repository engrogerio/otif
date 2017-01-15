# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0004_auto_20170108_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='business_unit',
            field=models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true'),
        ),
    ]
