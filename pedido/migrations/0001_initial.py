# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0001_initial'),
        ('cliente', '0001_initial'),
        ('falta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carregamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr_nota_fis', models.CharField(max_length=32, null=b'true', verbose_name=b'Nota fiscal', blank=b'true')),
                ('dt_saida', models.DateField(null=b'true', verbose_name=b'Data Programada', blank=b'true')),
                ('hr_grade', models.TimeField(null=b'true', verbose_name=b'Hor\xc3\xa1rio Programado', blank=b'true')),
                ('ds_placa', models.CharField(max_length=8, null=b'true', verbose_name=b'Placa do ve\xc3\xadculo', blank=b'true')),
                ('ds_transp', models.CharField(max_length=30, null=b'true', verbose_name=b'Nome da transportadora', blank=b'true')),
                ('nr_lacre', models.CharField(max_length=10, null=b'true', verbose_name=b'N\xc3\xbamero do lacre', blank=b'true')),
                ('dt_hr_chegada', models.DateTimeField(null=b'true', verbose_name=b'Chegada do caminh\xc3\xa3o', blank=b'true')),
                ('dt_hr_ini_carga', models.DateTimeField(null=b'true', verbose_name=b'Inicio do carregamento', blank=b'true')),
                ('dt_hr_fim_carga', models.DateTimeField(null=b'true', verbose_name=b'Fim do carregamento', blank=b'true')),
                ('dt_hr_liberacao', models.DateTimeField(null=b'true', verbose_name=b'Libera\xc3\xa7\xc3\xa3o do caminh\xc3\xa3o', blank=b'true')),
                ('ds_status_carrega', models.IntegerField(default=0, null=b'true', verbose_name=b'Status', blank=b'true', choices=[(0, b'Carregamento programado'), (1, b'Caminh\xc3\xa3o na planta'), (2, b'Carregamento iniciado'), (3, b'Carregamento finalizado'), (4, b'Caminh\xc3\xa3o liberado')])),
                ('ds_status_cheg', models.CharField(max_length=15, null=b'true', verbose_name=b'Status de chegada', blank=b'true')),
                ('ds_status_lib', models.CharField(max_length=15, null=b'true', verbose_name=b'Status de libera\xc3\xa7\xc3\xa3o', blank=b'true')),
                ('qt_pallet', models.IntegerField(null=b'true', verbose_name=b'Quantidade de Pallets', blank=b'true')),
                ('ds_obs_carga', models.TextField(max_length=500, null=b'true', verbose_name=b'Obs', blank=b'true')),
                ('id_no_show', models.IntegerField(default=2, verbose_name=b'No Show', choices=[(1, b'S'), (2, b'N')])),
                ('business_unit', models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true')),
                ('cliente', models.ForeignKey(db_column=b'nm_ab_cli', to_field=b'nm_ab_cli', blank=b'true', to='cliente.Cliente', null=b'true', verbose_name=b'Cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr_nota_fis', models.CharField(max_length=32, null=b'true', verbose_name=b'Nota fiscal', blank=b'true')),
                ('nr_pedido', models.CharField(max_length=24, null=b'true', verbose_name=b'Pedido do cliente', blank=b'true')),
                ('ds_ord_compra', models.CharField(max_length=15, null=b'true', verbose_name=b'Ordem de compra', blank=b'true')),
                ('cd_produto', models.CharField(max_length=32, null=b'true', verbose_name=b'C\xc3\xb3digo do produto', blank=b'true')),
                ('ds_produto', models.CharField(max_length=200, null=b'true', verbose_name=b'Descri\xc3\xa7\xc3\xa3o do produto', blank=b'true')),
                ('un_embalagem', models.CharField(max_length=3, null=b'true', verbose_name=b'Unidade de embalagem', blank=b'true')),
                ('qt_embalagem', models.IntegerField(null=b'true', verbose_name=b'Quantidade de embalagens', blank=b'true')),
                ('qt_pilha', models.CharField(max_length=10, null=b'true', verbose_name=b'Pilhas', blank=b'true')),
                ('qt_carregada', models.IntegerField(null=b'true', verbose_name=b'Quantidade carregada', blank=b'true')),
                ('qt_falta', models.IntegerField(null=b'true', verbose_name=b'Quantidade em falta', blank=b'true')),
                ('business_unit', models.ForeignKey(verbose_name=b'C\xc3\xb3d. Estab.', blank=b'true', to='business_unit.BusinessUnit', null=b'true')),
                ('carregamento', models.ForeignKey(to='pedido.Carregamento')),
                ('cliente', models.ForeignKey(db_column=b'nm_ab_cli', to_field=b'nm_ab_cli', blank=b'true', to='cliente.Cliente', null=b'true', verbose_name=b'Cliente')),
                ('motivo', models.ForeignKey(blank=b'true', to='falta.Motivo', null=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pallet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr_pallet', models.IntegerField(null=b'true', verbose_name=b'Nr. Pallet', blank=b'true')),
                ('carregamento', models.ForeignKey(related_name='carregamento_pallet', blank=b'true', to='pedido.Carregamento', null=b'true')),
            ],
        ),
        migrations.CreateModel(
            name='FillRate',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pedido.item',),
        ),
        migrations.CreateModel(
            name='NoShow',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pedido.carregamento',),
        ),
    ]
