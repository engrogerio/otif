# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_auto_20170110_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='business_unit',
            field=models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='business_unit',
            field=models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true'),
        ),
    ]
