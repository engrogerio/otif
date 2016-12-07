# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0007_auto_20161127_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='id_no_show',
            field=models.IntegerField(default=2, verbose_name=b'No Show', choices=[(1, b'S'), (2, b'N')]),
        ),
    ]
