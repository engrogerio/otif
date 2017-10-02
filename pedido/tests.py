# -*- encoding: utf-8 -*-

from django.test import TestCase
from pedido.models import Carregamento
from cliente.models import Cliente
from business_unit.models import BusinessUnit

class CarregamentoStatusTestCase(TestCase):

    def setUp(self):
        """Cria uma unidade, um cliente e um carregamento para os testes"""
        BusinessUnit.objects.create(
            cd_unit ='01',
            unit = 'TATUI')

        Cliente.objects.create(
            nm_ab_cli='FFJDI',
            ds_classe_cli = '',
            hr_lim_carga = '2:00',
            hr_lim_lib = '3:00')

        Carregamento.objects.create(
            business_unit = BusinessUnit.objects.get(cd_unit='01'),
            cliente = Cliente.objects.get(nm_ab_cli='FFJDI'),
            nr_nota_fis = '22',
            nr_pedido = 2222,
            ds_ord_compra = 3333,
            dt_saida = '2017-01-01',
            hr_grade = '10:00:00',
            ds_placa = 'XXX9999',
            ds_transp = 'TRANSPBRASIL',
            nr_lacre = '666',
            dt_hr_chegada = None,
            dt_hr_ini_carga = None,
            dt_hr_fim_carga = None,
            dt_hr_liberacao = None,
            ds_status_carrega = 0,
            ds_status_cheg = '',  # a calcular
            ds_status_lib = '',  # a calcularcarregamento
            qt_pallet = 2,
            ds_obs_carga = 'Teste automatico',
            id_no_show = Carregamento.SIM,
            pallets = '3 4',
            cd_rota = '1')

    def test_alteracao_status(self):
        """ Alteração de Status do carregamento deve alterar o campo de status corretamente"""
        c1 = Carregamento.objects.get(nr_nota_fis='22')
        self.assertEqual(c1.ds_status_carrega, Carregamento.PROGRAMADO)

        c1.set_chegada(date='2017-01-01 11:00:00', grade ='1:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.ds_status_carrega, Carregamento.NA_PLANTA)

        c1.set_inicio(date='2017-01-01 11:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.ds_status_carrega, Carregamento.INICIO)

        c1.set_fim(date='2017-01-01 11:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.ds_status_carrega, Carregamento.FIM)

        c1.set_libera(date='2017-01-01 11:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.ds_status_carrega, Carregamento.LIBERADO)

    def test_alteracao_data_chegada(self):
        """Alteração de horário e data de cada status no botão de ação da tela inicial"""
        c1 = Carregamento.objects.get(nr_nota_fis='22')

        c1.set_chegada(date='2017-01-01 11:00:00', grade ='1:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_hr_chegada,'2017-01-01 11:00:00')

        c1.set_chegada(date='2017-02-01 0:00:00', grade ='1:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_hr_chegada, '2017-02-01 0:00:00')

        c1.set_inicio(date='2017-01-01 11:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_hr_ini_carga, '2017-01-01 11:00:00')

        c1.set_inicio(date='2017-03-01 1:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_hr_ini_carga, '2017-03-01 1:00:00')

        c1.set_fim(date='2017-01-01 11:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_hr_fim_carga, '2017-01-01 11:00:00')

        c1.set_fim(date='2018-01-01 15:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_hr_fim_carga, '2018-01-01 15:00:00')

        c1.set_libera(date='2017-01-01 11:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_hr_liberacao, '2017-01-01 11:00:00')

        c1.set_libera(date='2017-12-31 23:59:59', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_hr_liberacao, '2017-12-31 23:59:59')

    def test_chegada_no_horario(self):
        """Caminhoes chegando dentro da tolerância de horário"""
        c1 = Carregamento.objects.get(nr_nota_fis='22')
        c1.set_chegada(date='2017-01-01 12:00:00', grade = None, placa='1111', lacre='1111', )
        self.assertEqual(c1.get_status_cheg(),'No Hor\xc3\xa1rio')

    def test_chegada_atrasado(self):
        """Caminhoes chegando fora da tolerância de horário"""
        c1 = Carregamento.objects.get(nr_nota_fis='22')
        c1.set_chegada(date='2017-01-01 12:00:01', grade = None, placa='1111', lacre='1111', )
        self.assertEqual(c1.get_status_cheg(),'Atrasado')

    def test_liberacao_no_horario(self):
        """Caminhoes liberados dentro da tolerância de horário"""
        c1 = Carregamento.objects.get(nr_nota_fis='22')
        c1.set_libera(date='2017-01-01 13:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.get_status_lib(), 'No Hor\xc3\xa1rio')

    def test_liberacao_atrasado(self):
        """Caminhoes liberados fora da tolerância de horário"""
        c1 = Carregamento.objects.get(nr_nota_fis='22')
        c1.set_libera(date='2017-01-01 13:00:01', placa='1111', lacre='1111', )
        self.assertEqual(c1.get_status_lib(), 'Atrasado')

