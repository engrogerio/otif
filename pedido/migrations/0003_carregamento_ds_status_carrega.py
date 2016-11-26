# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_auto_20161124_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='carregamento',
            name='ds_status_carrega',
            field=models.IntegerField(blank=b'true', null=b'true', verbose_name=b'Status do carregamento', choices=[(1, b'Caminh\xc3\xa3o na planta'), (2, b'Carregamento iniciado'), (3, b'Carregamento finalizado'), (4, b'Caminh\xc3\xa3o liberado')]),
        ),
    ]
