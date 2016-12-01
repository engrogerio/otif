# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multa', '0001_initial'),
        ('pedido', '0006_auto_20161126_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carregamento',
            name='vl_base_multa',
        ),
        migrations.RemoveField(
            model_name='carregamento',
            name='vl_fixo',
        ),
        migrations.RemoveField(
            model_name='carregamento',
            name='vl_multa',
        ),
        migrations.RemoveField(
            model_name='item',
            name='vl_base_multa',
        ),
        migrations.RemoveField(
            model_name='item',
            name='vl_multa',
        ),
        migrations.AddField(
            model_name='carregamento',
            name='multa',
            field=models.ForeignKey(verbose_name=b'Multa', blank=b'true', to='multa.Carregamento', null=b'true'),
        ),
        migrations.AddField(
            model_name='item',
            name='multa',
            field=models.ForeignKey(verbose_name=b'Multa', blank=b'true', to='multa.Item', null=b'true'),
        ),
    ]