# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dt_atlz', models.DateTimeField(null=b'true', verbose_name=b'Data atualiza\xc3\xa7\xc3\xa3o', blank=b'true')),
                ('cd_estab', models.CharField(max_length=3, null=b'true', verbose_name=b'C\xc3\xb3digo do estab.', blank=b'true')),
                ('nr_nota_fis', models.CharField(max_length=32, null=b'true', verbose_name=b'N\xc3\xbamero da Nota fiscal', blank=b'true')),
                ('dt_saida', models.DateField(null=b'true', verbose_name=b'Data de sa\xc3\xadda do Carregamento', blank=b'true')),
                ('ds_placa', models.CharField(max_length=8, null=b'true', verbose_name=b'Placa do ve\xc3\xadculo', blank=b'true')),
                ('ds_transp', models.CharField(max_length=30, null=b'true', verbose_name=b'Nome da transportadora', blank=b'true')),
                ('nr_lacre', models.CharField(max_length=10, null=b'true', verbose_name=b'N\xc3\xbamero do lacre', blank=b'true')),
                ('dt_hr_chegada', models.DateTimeField(null=b'true', verbose_name=b'Chegada do caminh\xc3\xa3o', blank=b'true')),
                ('dt_hr_ini_carga', models.DateTimeField(null=b'true', verbose_name=b'Inicio do carregamento', blank=b'true')),
                ('dt_hr_fim_carga', models.DateTimeField(null=b'true', verbose_name=b'Fim do carregamento', blank=b'true')),
                ('dt_hr_liberacao', models.DateTimeField(null=b'true', verbose_name=b'Libera\xc3\xa7\xc3\xa3o do caminh\xc3\xa3o', blank=b'true')),
                ('ds_status_cheg', models.CharField(max_length=15, null=b'true', verbose_name=b'Status de chegada', blank=b'true')),
                ('ds_get_status_lib', models.CharField(max_length=15, null=b'true', verbose_name=b'Status de libera\xc3\xa7\xc3\xa3o', blank=b'true')),
                ('ds_obs_carga', models.CharField(max_length=500, null=b'true', verbose_name=b'Obs', blank=b'true')),
                ('id_no_show', models.CharField(default=b'N', max_length=1, verbose_name=b'No Show')),
                ('vl_fixo', models.DecimalField(null=b'true', verbose_name=b'Valor fixo da multa', max_digits=17, decimal_places=2, blank=b'true')),
                ('vl_base_multa', models.DecimalField(null=b'true', verbose_name=b'Valor base da multa', max_digits=17, decimal_places=2, blank=b'true')),
                ('vl_multa', models.DecimalField(null=b'true', verbose_name=b'Valor da multa', max_digits=17, decimal_places=2, blank=b'true')),
                ('st_chegada', models.CharField(default=b'No Hor\xc3\xa1rio', max_length=15, null=b'true', verbose_name=b'Status de Chegada', blank=b'true')),
                ('st_libera', models.CharField(default=b'No Hor\xc3\xa1rio', max_length=15, null=b'true', verbose_name=b'Status de Libera\xc3\xa7\xc3\xa3o', blank=b'true')),
                ('cliente', models.ForeignKey(db_column=b'nm_ab_cli', to_field=b'nm_ab_cli', blank=b'true', to='cliente.Cliente', null=b'true', verbose_name=b'Cliente')),
                ('grade', models.ForeignKey(verbose_name=b'Hora da grade do cliente', blank=b'true', to='grade.Grade', null=b'true')),
                ('usr_atlz', models.ForeignKey(blank=b'true', to=settings.AUTH_USER_MODEL, null=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dt_atlz', models.DateTimeField(null=b'true', verbose_name=b'Data atualiza\xc3\xa7\xc3\xa3o', blank=b'true')),
                ('cd_estab', models.CharField(max_length=3, null=b'true', verbose_name=b'C\xc3\xb3digo do estab.', blank=b'true')),
                ('nr_nota_fis', models.CharField(max_length=32, null=b'true', verbose_name=b'N\xc3\xbamero da Nota fiscal', blank=b'true')),
                ('nr_pedido', models.CharField(max_length=24, null=b'true', verbose_name=b'N\xc3\xbamero do pedido do cliente', blank=b'true')),
                ('ds_ord_compra', models.CharField(max_length=15, null=b'true', verbose_name=b'N\xc3\xbamero da ordem de compra', blank=b'true')),
                ('cd_produto', models.CharField(max_length=32, null=b'true', verbose_name=b'C\xc3\xb3digo do produto', blank=b'true')),
                ('un_embalagem', models.CharField(max_length=3, null=b'true', verbose_name=b'Unidade de embalagem', blank=b'true')),
                ('qt_embalagem', models.IntegerField(null=b'true', verbose_name=b'Quantidade de embalagens', blank=b'true')),
                ('qt_pilha', models.CharField(max_length=10, null=b'true', verbose_name=b'Quantidade da pilha', blank=b'true')),
                ('qt_carregada', models.IntegerField(null=b'true', verbose_name=b'Quantidade carregada', blank=b'true')),
                ('qt_falta', models.IntegerField(null=b'true', verbose_name=b'Quantidade em falta', blank=b'true')),
                ('id_motivo', models.IntegerField(null=b'true', verbose_name=b'Motivo', blank=b'true')),
                ('qt_pallet', models.IntegerField(null=b'true', verbose_name=b'Quantidade de Pallets', blank=b'true')),
                ('vl_base_multa', models.DecimalField(null=b'true', verbose_name=b'Valor base da multa', max_digits=17, decimal_places=2, blank=b'true')),
                ('vl_multa', models.DecimalField(null=b'true', verbose_name=b'Valor da multa', max_digits=17, decimal_places=2, blank=b'true')),
                ('base', models.ForeignKey(to='pedido.Base')),
                ('cliente', models.ForeignKey(db_column=b'nm_ab_cli', to_field=b'nm_ab_cli', blank=b'true', to='cliente.Cliente', null=b'true', verbose_name=b'Cliente')),
                ('usr_atlz', models.ForeignKey(blank=b'true', to=settings.AUTH_USER_MODEL, null=b'true')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
