# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_auto_20170801_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='business_unit',
            field=models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='cliente',
            field=models.ForeignKey(verbose_name=b'Cliente', blank=b'true', to='cliente.Cliente', null=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_obs_carga',
            field=models.CharField(max_length=500, null=b'true', verbose_name=b'Obs', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_ord_compra',
            field=models.CharField(max_length=15, null=b'true', verbose_name=b'Ordem compra', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_placa',
            field=models.CharField(max_length=8, null=b'true', verbose_name=b'Placa do ve\xc3\xadculo', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_carrega',
            field=models.IntegerField(default=0, null=b'true', verbose_name=b'Status', blank=b'true', choices=[(0, b'Carregamento programado'), (1, b'Caminh\xc3\xa3o na planta'), (2, b'Carregamento iniciado'), (3, b'Carregamento finalizado'), (4, b'Caminh\xc3\xa3o liberado')]),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_cheg',
            field=models.CharField(max_length=15, null=b'true', verbose_name=b'Status de chegada', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_status_lib',
            field=models.CharField(max_length=15, null=b'true', verbose_name=b'Status de libera\xc3\xa7\xc3\xa3o', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='ds_transp',
            field=models.CharField(max_length=30, null=b'true', verbose_name=b'Transportadora', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_hr_chegada',
            field=models.DateTimeField(null=b'true', verbose_name=b'Chegada do caminh\xc3\xa3o', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_hr_fim_carga',
            field=models.DateTimeField(null=b'true', verbose_name=b'Fim do carregamento', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_hr_ini_carga',
            field=models.DateTimeField(null=b'true', verbose_name=b'Inicio do carregamento', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_hr_liberacao',
            field=models.DateTimeField(null=b'true', verbose_name=b'Libera\xc3\xa7\xc3\xa3o do caminh\xc3\xa3o', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='dt_saida',
            field=models.DateField(null=b'true', verbose_name=b'Data Programada', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='hr_grade',
            field=models.TimeField(null=b'true', verbose_name=b'Hor\xc3\xa1rio', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='id_no_show',
            field=models.IntegerField(blank=b'true', null=b'true', verbose_name=b'No Show', choices=[(1, b'S'), (2, b'N')]),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='nr_lacre',
            field=models.CharField(max_length=10, null=b'true', verbose_name=b'N\xc3\xbamero do lacre', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='nr_nota_fis',
            field=models.CharField(max_length=32, null=b'true', verbose_name=b'Nota fiscal', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='nr_pedido',
            field=models.CharField(max_length=24, null=b'true', verbose_name=b'Pedido', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='pallets',
            field=models.CharField(max_length=1000, null=b'true', verbose_name=b'Pallets', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='business_unit',
            field=models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cd_produto',
            field=models.CharField(max_length=32, null=b'true', verbose_name=b'C\xc3\xb3digo do produto', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ds_produto',
            field=models.CharField(max_length=200, null=b'true', verbose_name=b'Descri\xc3\xa7\xc3\xa3o do produto', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='motivo',
            field=models.ForeignKey(blank=b'true', to='falta.Motivo', null=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='qt_pilha',
            field=models.CharField(max_length=10, null=b'true', verbose_name=b'Pilhas', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='item',
            name='un_embalagem',
            field=models.CharField(max_length=3, null=b'true', verbose_name=b'Unidade de embalagem', blank=b'true'),
        ),
    ]
