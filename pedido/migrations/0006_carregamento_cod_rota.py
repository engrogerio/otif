# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_auto_20170803_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='carregamento',
            name='cd_rota',
            field=models.CharField(max_length=10, null=b'true', verbose_name=b'Rota', blank=b'true'),
        ),
    ]
