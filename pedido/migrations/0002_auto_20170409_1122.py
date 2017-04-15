# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pallet',
            name='carregamento',
        ),
        migrations.AddField(
            model_name='carregamento',
            name='pallets',
            field=models.CharField(max_length=1000, null=b'true', verbose_name=b'Pallets', blank=b'true'),
        ),
        migrations.DeleteModel(
            name='Pallet',
        ),
    ]
