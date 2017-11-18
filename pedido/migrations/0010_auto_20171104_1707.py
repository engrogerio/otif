# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta', '0004_motivoalteraagenda'),
        ('pedido', '0009_auto_20171103_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='carregamento',
            name='ds_obs_agenda',
            field=models.CharField(max_length=500, null=b'true', verbose_name=b'Obs', blank=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='ds_status_cheg_cliente',
            field=models.CharField(max_length=15, null=b'true', verbose_name=b'Status de chegada no cliente', blank=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='dt_hr_agenda',
            field=models.DateTimeField(null=b'true', verbose_name=b'Agendamento da entrega', blank=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='dt_hr_cheg_cliente',
            field=models.DateTimeField(null=b'true', verbose_name=b'Chegada no cliente', blank=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='dt_hr_descarrega',
            field=models.DateTimeField(null=b'true', verbose_name=b'Descarregamento', blank=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='motivo_altera_agenda',
            field=models.ForeignKey(blank=b'true', to='falta.MotivoDeAlteracaoDaAgenda', null=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='protocolo_agenda',
            field=models.CharField(max_length=100, null=b'true', verbose_name=b'Protocolo do agendamento', blank=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='tipo_frete',
            field=models.CharField(max_length=5, null=b'true', verbose_name=b'Frete', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_carrega',
            field=models.IntegerField(default=0, null=b'true', verbose_name=b'Status', blank=b'true', choices=[(0, b'Carregamento programado'), (1, b'Caminh\xc3\xa3o na planta'), (2, b'Carregamento iniciado'), (3, b'Carregamento finalizado'), (4, b'Caminh\xc3\xa3o liberado'), (5, b'Caminh\xc3\xa3o no cliente'), (6, b'Pedido entregue')]),
        ),
    ]
