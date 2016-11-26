# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_carregamento_ds_status_carrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_carrega',
            field=models.IntegerField(blank=b'true', null=b'true', verbose_name=b'Status', choices=[(1, b'Caminh\xc3\xa3o na planta'), (2, b'Carregamento iniciado'), (3, b'Carregamento finalizado'), (4, b'Caminh\xc3\xa3o liberado')]),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='nr_nota_fis',
            field=models.CharField(max_length=32, null=b'true', verbose_name=b'Nota fiscal', blank=b'true'),
        ),
    ]
