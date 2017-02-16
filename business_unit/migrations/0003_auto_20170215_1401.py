# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0002_auto_20170214_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_estabelecimento',
            name='unit',
            field=models.ForeignKey(related_name='unit_estabelecimento', default=1, verbose_name=b'C\xc3\xb3d. Estab.', to='business_unit.BusinessUnit'),
            preserve_default=False,
        ),
    ]
