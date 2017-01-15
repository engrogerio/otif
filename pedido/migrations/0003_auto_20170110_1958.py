# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0008_auto_20170110_1958'),
        ('pedido', '0002_auto_20170108_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='carregamento',
            name='business_unit',
            field=models.ForeignKey(blank=b'true', to='business_unit.BusinessUnit', null=b'true'),
        ),
        migrations.AddField(
            model_name='item',
            name='business_unit',
            field=models.ForeignKey(blank=b'true', to='business_unit.BusinessUnit', null=b'true'),
        ),
    ]
