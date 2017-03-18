# -*- encoding: utf-8 -*-

from django.db import models
from sgo.models import OtifModel
from grade.models import Grade
from cliente.models import Cliente
import datetime
from falta.models import Motivo
from business_unit.models import BusinessUnitSpecificModel

# TODO: Atualizar a documentação
"""
Modelo de pedidos importados do Totvs ERP via arquivo txt.
Dados importados não estão normalizados.
Modelo possue dados de Cliente, Produtos, Pedidos, NF e Transportadora

Aplicação: Otif

    Modelo: OtifModel (base para todas os modelos)
        dt_atlz
        id_usr_atlz

Aplicação: Pedido

    Modelo: Carregamento
        business_unit       Código do estabelecimento (JDF, STO, JAG ou OSA)
        nm_ab_cliente       Código do cliente
        nr_nota_fis         Número da Nota fiscal
        nr_pedido           Número do pedido do cliente
        ds_ordem_compra     Número da ordem de compra
        ds_placa            Placa do veículo
        ds_transp           Nome da transportadora
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
        id_no_show          S ou N
        vl_fixo             Valor fixo da multa
        vl_base_multa       Valor base da multa
        vl_multa            Calculado (Se "id_no_show" = S então (("Valor base
                            multa" * 0,05)+"vl_fixo") senão, 0)

    Modelo: Item
        business_unit       Código do estabelecimento (JDF, STO, JAG ou OSA)
        nm_ab_cliente       Código do cliente
        nr_nota_fis         Número da Nota fiscal
        dt_saida            Data de saída do pedido
        hr_grade            Hora da grade do cliente
        cd_produto          Código do produto
        un_embalagem        Unidade de embalagem
        qt_embalagem        Quantidade de embalagens
        qt_pilha            Quantidade da pilha
        qt_carregada        Quantidade carregada
        qt_falta            Quantidade faltante
        id_motivo
        qt_pallet           Quantidade de pallets
        vl_base_multa       Valor base da multa
        vl_multa            Calculado (Se "id_no_show" = S então (("Valor base
                            multa" * 0,05)+"vl_fixo") senão, 0)
"""



class Carregamento(BusinessUnitSpecificModel):

    PROGRAMADO = 0
    NA_PLANTA = 1
    INICIO = 2
    FIM = 3
    LIBERADO = 4
    STATUS=(
        (PROGRAMADO,'Carregamento programado'),
        (NA_PLANTA,'Caminhão na planta'),
        (INICIO, 'Carregamento iniciado'),
        (FIM, 'Carregamento finalizado'),
        (LIBERADO, 'Caminhão liberado')
    )

    SIM=1
    NAO=2
    NO_SHOW=(
        (SIM,'S'),
        (NAO,'N')
    )
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', blank='true', null='true', )
    nr_nota_fis = models.CharField('Nota fiscal', max_length=32, null='true', blank='true', )
    nr_pedido = models.CharField('Pedido', max_length=24, null='true', blank='true', )
    ds_ord_compra = models.CharField('Ordem compra', max_length=15, null='true', blank='true', )
    dt_saida = models.DateField('Data Programada', null='true', blank='true', )
    hr_grade = models.TimeField('Horário', null='true', blank='true',)
    ds_placa = models.CharField('Placa do veículo', max_length=8, null='true', blank='true', )
    ds_transp = models.CharField('Transportadora', max_length=30, null='true', blank='true', )
    nr_lacre = models.CharField('Número do lacre', max_length=10, null='true', blank='true', )
    dt_hr_chegada = models.DateTimeField('Chegada do caminhão', null='true', blank='true', )
    dt_hr_ini_carga = models.DateTimeField('Inicio do carregamento', null='true', blank='true', )
    dt_hr_fim_carga = models.DateTimeField('Fim do carregamento', null='true', blank='true', )
    dt_hr_liberacao = models.DateTimeField('Liberação do caminhão', null='true', blank='true', )
    ds_status_carrega = models.IntegerField('Status', choices=STATUS, default=PROGRAMADO, null='true', blank='true')
    ds_status_cheg = models.CharField('Status de chegada', max_length=15, null='true', blank='true')
    ds_status_lib = models.CharField('Status de liberação', max_length=15, null='true', blank='true')
    qt_pallet = models.IntegerField('Quantidade de Pallets', null='true', blank='true', )
    ds_obs_carga = models.CharField('Obs', max_length=500, null='true', blank='true', )
    id_no_show = models.IntegerField('No Show', choices= NO_SHOW, null='true', blank='true',)

    def __unicode__(self):
        return '' or ''.join([self.cliente.nm_ab_cli, self.nr_nota_fis])

    def set_chegada(self):
        self.dt_hr_chegada=datetime.datetime.now()
        self.ds_status_carrega = self.NA_PLANTA
        self.ds_status_cheg=self.get_status_cheg()
        #self.id_no_show = self.NAO
        self.save()

    def set_inicio(self):
        self.dt_hr_ini_carga=datetime.datetime.now()
        self.ds_status_carrega = self.INICIO
        self.save()

    def set_fim(self):
        self.dt_hr_fim_carga=datetime.datetime.now()
        self.ds_status_carrega = self.FIM
        self.save()

    def set_libera(self):
        self.dt_hr_liberacao=datetime.datetime.now()
        self.ds_status_carrega = self.LIBERADO
        self.ds_status_lib=self.get_status_lib()
        self.save()

    def get_status_cheg(self):
        """Calculado(Se Hr de chegada > (data e Hr Grade - Limite carga da tabela ARZ_LIMITE_CLIENTE) então "Atrasado"
        senão "No Horário")"""
        # se não está programada a data ou hora do pedido, é inserido automaticamente a data e hora atuais como plano
        if not self.hr_grade:
            self.hr_grade=datetime.time(datetime.datetime.now().time().hour,datetime.datetime.now().time().minute)
        if not self.dt_saida:
            self.dt_saida=datetime.datetime.now().date()

        dt_previsao = (datetime.datetime.combine(self.dt_saida, self.hr_grade))
        # baseado no limite de carregamento do cliente, calcula a data/hora máxima para não ser considerado atraso
        # Se não foi cadastrado limite para o carregamento, considera 0
        try:
            delta = datetime.timedelta( hours=self.cliente.limite.hr_lim_carga.hour
                or 0, minutes =self.cliente.limite.hr_lim_carga.minute or 0)
        except:
            delta = datetime.timedelta(hours=0, minutes=0)
        dt_maxima = dt_previsao-delta
        if self.dt_hr_chegada > dt_maxima:
            return "Atrasado"
        else:
            return "No Horário"

    def get_status_lib(self):
        """Calculado(Se Hr de liberação > (data e Hr Grade + Limite liberação da tabela ARZ_LIMITE_CLIENTE) então
        "Atrasado" senão "No Horário")"""
        # se não está programada a data ou hora do pedido, é inserido automaticamente a data e hora atuais como plano
        if not self.hr_grade:
            self.hr_grade = datetime.time(datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)
        if not self.dt_saida:
            self.dt_saida = datetime.datetime.now().date()
        dt_previsao = (datetime.datetime.combine(self.dt_saida, self.hr_grade))
        # baseado no limite do cliente, calcula a data/hora máxima para não ser considerado atraso
        # Se não foi cadastrado limite para de liberação, considera 0
        try:
            delta = datetime.timedelta(hours=self.cliente.hr_lim_lib.hour or 0,
                minutes=self.cliente.hr_lim_lib.minute or 0)
        except:
            delta = datetime.timedelta(hours=0, minutes=0)
        dt_maxima = dt_previsao + delta
        if self.dt_hr_liberacao > dt_maxima:
            return "Atrasado"
        else:
            return "No Horário"

        # TODO:
        # def save(self):
        #     """
        #     Cria um popup com campos para preencher os números dos pallets para
        #         cada pedido conforme qt_pallet.
        #     """
        #     super(Item, self).save()

class Item(BusinessUnitSpecificModel):

    cd_produto = models.CharField('Código do produto', max_length=32, null='true', blank='true', )
    ds_produto = models.CharField('Descrição do produto', max_length=200, null='true', blank='true')
    un_embalagem = models.CharField('Unidade de embalagem', max_length=3, null='true', blank='true', )
    qt_embalagem = models.IntegerField('Quantidade de embalagens', default=0, )
    qt_pilha = models.CharField('Pilhas', max_length=10, null='true', blank='true', )
    qt_carregada = models.IntegerField('Quantidade carregada', default=0, )
    # qt_falta = models.IntegerField('Quantidade em falta', null='true', blank='true', )
    motivo = models.ForeignKey(Motivo, null='true', blank='true', )
    carregamento = models.ForeignKey(Carregamento, related_name='carregamento_items')

    @property
    def qt_falta(self):
        return self.qt_embalagem - self.qt_carregada

    def __unicode__(self):
        return self.ds_produto or ''


class Pallet(models.Model):
    carregamento = models.ForeignKey(Carregamento, null='true', blank='true', related_name='carregamento_pallet')
    nr_pallet = models.IntegerField('Nr. Pallet',  null='true', blank='true')
    def __unicode__(self):
        return self.nr_pallet


class FillRate(Item):
    class Meta:
        proxy = True


class NoShow(Carregamento):
    class Meta:
        proxy = True