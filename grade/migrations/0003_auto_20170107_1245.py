# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_grade_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='unit',
            field=models.ForeignKey(verbose_name=b'Unidade', to='business_unit.BusinessUnit'),
        ),
    ]
