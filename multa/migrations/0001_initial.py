# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultaCarregamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vl_multa', models.DecimalField(null=b'true', verbose_name=b'Valor da multa (R$)', max_digits=17, decimal_places=2, blank=b'true')),
                ('carregamento', models.ForeignKey(related_name='carregamento_multa', blank=b'true', to='pedido.Carregamento', null=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultaItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vl_multa', models.DecimalField(null=b'true', verbose_name=b'Valor da multa (R$)', max_digits=17, decimal_places=2, blank=b'true')),
                ('item', models.ForeignKey(related_name='item_multa', blank=b'true', to='pedido.Item', null=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
