# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='id_no_show',
            field=models.IntegerField(blank=b'true', null=b'true', verbose_name=b'No Show', choices=[(1, b'S'), (2, b'N')]),
        ),
    ]
