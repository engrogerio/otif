# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta', '0003_auto_20170803_1901'),
        ('business_unit', '0003_auto_20170803_1901'),
        ('pedido', '0006_carregamento_cod_rota'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivosAtrasoCarregamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ds_obs', models.CharField(max_length=300, verbose_name=b'Observa\xc3\xa7\xc3\xa3o')),
                ('business_unit', models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true')),
                ('carregamento', models.ForeignKey(verbose_name=b'Carregamento', blank=b'true', to='pedido.Carregamento', null=b'true')),
                ('motivo', models.ForeignKey(verbose_name=b'Motivo', blank=b'true', to='falta.Motivo', null=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
