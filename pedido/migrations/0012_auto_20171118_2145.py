# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0011_auto_20171109_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_carrega',
            field=models.IntegerField(default=0, null=b'true', verbose_name=b'Status', blank=b'true', choices=[(0, b'Carregamento sem programa\xc3\xa7\xc3\xa3o'), (1, b'Carregamento programado'), (2, b'Caminh\xc3\xa3o na planta'), (3, b'Carregamento iniciado'), (4, b'Carregamento finalizado'), (5, b'Caminh\xc3\xa3o liberado'), (6, b'Caminh\xc3\xa3o no cliente'), (7, b'Pedido entregue')]),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='motivo_altera_agenda',
            field=models.ForeignKey(verbose_name=b'Motivo da altera\xc3\xa7\xc3\xa3o da agenda', blank=b'true', to='falta.MotivoDeAlteracaoDaAgenda', null=b'true'),
        ),
    ]
