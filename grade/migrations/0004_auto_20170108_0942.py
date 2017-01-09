# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0003_auto_20170107_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='business_unit',
            field=models.ForeignKey(verbose_name=b'Unidade', to='business_unit.BusinessUnit'),
        ),
    ]
