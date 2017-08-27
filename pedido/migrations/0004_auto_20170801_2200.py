# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_auto_20170415_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='business_unit',
            field=models.ForeignKey(verbose_name='Cód. Estab.', to='business_unit.BusinessUnit', blank='true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='cliente',
            field=models.ForeignKey(verbose_name='Cliente', to='cliente.Cliente', blank='true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_obs_carga',
            field=models.CharField(blank='true', verbose_name='Obs', max_length=500),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_ord_compra',
            field=models.CharField(blank='true', verbose_name='Ordem compra', max_length=15),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_placa',
            field=models.CharField(blank='true', verbose_name='Placa do veículo', max_length=8),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_carrega',
            field=models.IntegerField(blank='true', default=0, choices=[(0, 'Carregamento programado'), (1, 'Caminhão na planta'), (2, 'Carregamento iniciado'), (3, 'Carregamento finalizado'), (4, 'Caminhão liberado')], verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_cheg',
            field=models.CharField(blank='true', verbose_name='Status de chegada', max_length=15),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_lib',
            field=models.CharField(blank='true', verbose_name='Status de liberação', max_length=15),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_transp',
            field=models.CharField(blank='true', verbose_name='Transportadora', max_length=30),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_hr_chegada',
            field=models.DateTimeField(blank='true', verbose_name='Chegada do caminhão'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_hr_fim_carga',
            field=models.DateTimeField(blank='true', verbose_name='Fim do carregamento'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_hr_ini_carga',
            field=models.DateTimeField(blank='true', verbose_name='Inicio do carregamento'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_hr_liberacao',
            field=models.DateTimeField(blank='true', verbose_name='Liberação do caminhão', ),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_saida',
            field=models.DateField(blank='true', verbose_name='Data Programada', ),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='hr_grade',
            field=models.TimeField(blank='true', verbose_name='Horário'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='id_no_show',
            field=models.IntegerField(blank='true', verbose_name='No Show', choices=[(1, 'S'), (2, 'N')]),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='nr_lacre',
            field=models.CharField(blank='true', verbose_name='Número do lacre', max_length=10),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='nr_nota_fis',
            field=models.CharField(blank='true', verbose_name='Nota fiscal', max_length=32),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='nr_pedido',
            field=models.CharField(blank='true', verbose_name='Pedido', max_length=24),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='pallets',
            field=models.CharField(blank='true', verbose_name='Pallets', max_length=1000),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='qt_pallet',
            field=models.IntegerField(default=0, verbose_name='Quantidade de Pallets'),
        ),
        migrations.AlterField(
            model_name='item',
            name='business_unit',
            field=models.ForeignKey(verbose_name='Cód. Estab.', to='business_unit.BusinessUnit', blank='true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cd_produto',
            field=models.CharField(blank='true', verbose_name='Código do produto', max_length=32),
        ),
        migrations.AlterField(
            model_name='item',
            name='ds_produto',
            field=models.CharField(blank='true', verbose_name='Descrição do produto', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='motivo',
            field=models.ForeignKey(to='falta.Motivo', blank='true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='qt_carregada',
            field=models.IntegerField(default=0, verbose_name='Quantidade carregada'),
        ),
        migrations.AlterField(
            model_name='item',
            name='qt_embalagem',
            field=models.IntegerField(default=0, verbose_name='Quantidade de embalagens'),
        ),
        migrations.AlterField(
            model_name='item',
            name='qt_pilha',
            field=models.CharField(blank='true', verbose_name='Pilhas',max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='un_embalagem',
            field=models.CharField(blank='true', verbose_name='Unidade de embalagem', max_length=3),
        ),
    ]
