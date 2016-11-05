# -*- encoding: utf-8 -*-
from django.db import models
from sgo.models import OtifModel
from pedido.models import Base as PedidoBase
from pedido.models import Item as PedidoItem
from cadastro.models import Transportadora


"""
Aplicação: Carregamento

    Modelo: Base
        pedido_base         relacionamento com Base do pedido
        ds_placa            Placa do veículo
        transportadora      relacionamento com transportadora
        nr_lacre            Número do Lacre
        dt_hr_chegada       Data e Hora da chegada
        dt_hr_ini_carga     Data e Hora do inicio do carregamento
        dt_hr_fim_carga     Data e Hora do fim do carregamento
        dt_hr_liberacao     Data e Hora da liberação do caminhão

        ds_status_cheg      Calculado (Se hr_chegada > (data e Hr Grade - Limite carga da tabela
                            ARZ_LIMITE_CLIENTE) então "Atrasado" senão "No Horário")

        ds_status_lib       Calculado (Se Hr de Liberação > (data e Hr Grade + Limite Liberacao da tabela
                            ARZ_LIMITE_CLIENTE) então "Atrasado" senão "No Horário")

        ds_obs_carga        Conteúdo livre


    Modelo: Item
        carregamento_base   relacionamento com a base do carregamento
        qt_carregada        Quantidade do ítem carregada
        qt_falta            pedido.qtd_unidade-qtd_carregada
        qt_pallet           quantidade de pallets carregada


    Modelo: Multa
        carregamento_base   relacionamento com base do carregamento
        id_no_show          S ou N
        vl_base_multa       Valor base da multa
        vl_fixo             Valor fixo da multa
        vl_multa            Calculado (Se "id_no_show" = S então (("Valor base
                            multa" * 0,05)+"vl_fixo") senão, 0)

        ds_multa            Descrição do tipo de multa: "Fill Rate" ou "No Show"
        ds_motivo           Conteúdo livre

"""



class Base(OtifModel):

    pedido_base = models.ForeignKey(PedidoBase, null='true', blank='true', )
    ds_placa = models.CharField('Placa do veículo', max_length=3, null='true', blank='true', )
    transportadora = models.ForeignKey(Transportadora, null='true', blank='true', )
    nr_lacre = models.CharField('Número do Lacre', max_length=3, null='true', blank='true', )
    dt_hr_chegada = models.DateTimeField('Data e Hora da chegada', null='true', blank='true', )
    dt_hr_ini_carga = models.DateTimeField('Data e Hora do inicio do carregamento', null='true', blank='true', )
    dt_hr_fim_carga = models.DateTimeField('Data e Hora do fim do carregamento', null='true', blank='true', )
    dt_hr_liberacao = models.DateTimeField('Data e Hora da liberação do caminhão', null='true', blank='true', )
    #ds_status_cheg = get_status_cheg()
    #ds_status_lib = get_status_lib()
    ds_obs_carga = models.CharField('Código do estabelecimento', max_length=3, null='true', blank='true', )

    @property
    def ds_status_cheg(self):
        pass

    @property
    def ds_get_status_lib(self):
        pass

    def __str__(self):
        return self.nr_pedido


class Item(OtifModel):
    carregamento_base = models.ForeignKey(Base, null='true', blank='true', )
    pedido_item = models.ForeignKey(PedidoItem)
    qt_carregada = models.IntegerField('Quantidade carregada', null='true', blank='true', )
    qt_falta = models.IntegerField('Quantidade', null='true', blank='true', )

def __unicode__(self):
    return self.cd_produto
