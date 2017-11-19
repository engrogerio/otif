# -*- encoding: utf-8 -*-

from django.test import TestCase
from pedido.models import Carregamento
from cliente.models import Cliente
from business_unit.models import BusinessUnit
import datetime

class CarregamentoStatusTestCase(TestCase):

    def setUp(self):
        """Cria uma unidade, um cliente e um carregamento para os testes"""
        BusinessUnit.objects.create(
            cd_unit ='01',
            unit = 'JDF')

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
            #ds_status_carrega = 0 default value
            ds_status_cheg = '',  # a calcular
            ds_status_lib = '',  # a calcularcarregamento
            qt_pallet = 2,
            ds_obs_carga = 'Teste automatico',
            id_no_show = Carregamento.SIM,
            pallets = '3 4',
            cd_rota = '1',
            
            tipo_frete = 'CIF' ,
            dt_hr_agenda = None,
            dt_hr_cheg_cliente = None,
            dt_hr_descarrega = None,
            motivo_altera_agenda = None,
            protocolo_agenda = 'TESTE AGENDAMENTO',
            ds_obs_agenda = None,
            )

        Carregamento.objects.create(
            business_unit = BusinessUnit.objects.get(cd_unit='01'),
            cliente = Cliente.objects.get(nm_ab_cli='FFJDI'),
            nr_nota_fis = '11',
            nr_pedido = 1111,
            ds_ord_compra = 6666,
            dt_saida = None,
            hr_grade =  None,
            ds_placa = 'XXX9999',
            ds_transp = 'VAILONGETRANSP',
            nr_lacre = '666',
            dt_hr_chegada = None,
            dt_hr_ini_carga = None,
            dt_hr_fim_carga = None,
            dt_hr_liberacao = None,
            # ds_status_carrega = 0 Default value
            ds_status_cheg = '',  # a calcular
            ds_status_lib = '',  # a calcularcarregamento
            qt_pallet = 3,
            ds_obs_carga = 'Teste automatico 2',
            id_no_show = Carregamento.SIM,
            pallets = '1, 2, 3',
            cd_rota = '5',
            
            tipo_frete = 'FOB',
            dt_hr_agenda = None,
            dt_hr_cheg_cliente = None,
            dt_hr_descarrega = None,
            motivo_altera_agenda = None,
            protocolo_agenda = 'TESTE AGENDAMENTO',
            ds_obs_agenda = None,
            )

    
    def test_agenda_horario_fob(self):
        """
        Alteração de agenda deve retornar sempre "No horário" para carregamentos FOB
        """
        c1 = Carregamento.objects.get(nr_nota_fis='11')
        c1.dt_hr_agenda ='2017-01-01 00:00:00'
        c1.dt_hr_cheg_cliente ='2017-01-01 10:00:00'
        c1.set_chega_cliente()

        self.assertEqual(c1.ds_status_carrega, Carregamento.NO_CLIENTE)
        self.assertEqual(c1.ds_status_cheg_cliente, 'No Horário')        

    def test_agenda_horario_cif(self):
        """
        Alteração de agenda deve comparar a dt_hr_cheg_cliente com a dt_hr_agenda
        quando dt_hr_cheg_cliente <= dt_hr_agenda o campo ds_status_cheg_cliente
        deve ser "No horário"
        """
        c1 = Carregamento.objects.get(nr_nota_fis='22')
        c1.dt_hr_agenda ='2017-01-01 00:00:00'
        c1.dt_hr_cheg_cliente ='2017-01-01 00:00:00'
        c1.set_chega_cliente()

        self.assertEqual(c1.ds_status_carrega, Carregamento.NO_CLIENTE)
        self.assertEqual(c1.ds_status_cheg_cliente, 'No Horário')

    def test_agenda_atraso_cif(self):
        """
        Alteração de agenda deve comparar a dt_hr_cheg_cliente com a dt_hr_agenda
        quando dt_hr_cheg_cliente > dt_hr_agenda o campo ds_status_cheg_cliente
        deve ser "Em atraso".
        """
        c1 = Carregamento.objects.get(nr_nota_fis='22')
        c1.dt_hr_agenda ='2017-01-01 00:00:00'
        c1.dt_hr_cheg_cliente ='2017-01-01 00:00:01'
        c1.set_chega_cliente()

        self.assertEqual(c1.ds_status_carrega, Carregamento.NO_CLIENTE)
        self.assertEqual(c1.ds_status_cheg_cliente, 'Atrasado')


    def test_alteracao_status(self):
        """ Alteração de Status do carregamento deve alterar o campo de status corretamente"""
        c1 = Carregamento.objects.get(nr_nota_fis='22')
        self.assertEqual(c1.ds_status_carrega, Carregamento.SEM_PROGRAMACAO)

        c1.set_chegada(date='2017-01-01 11:00:00', grade ='1:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.ds_status_carrega, Carregamento.NA_PLANTA)

        c1.set_inicio(date='2017-01-01 11:00:00', placa='1111', lacre='1111', is_pre_carregamento=False )
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

        c1.set_inicio(date='2017-01-01 11:00:00', placa='1111', lacre='1111', is_pre_carregamento=False )
        self.assertEqual(c1.dt_hr_ini_carga, '2017-01-01 11:00:00')

        c1.set_inicio(date='2017-03-01 1:00:00', placa='1111', lacre='1111', is_pre_carregamento=False )
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

    """
    Para chegada do caminhão, temos a data de previsão (dt_saida), a grade(hr_grade) e a data e hora efetiva
     de chegada (dt_hr_chegada)
     Temos que testar na chegada:
        1- Chegada já tem data e hora prevista
        2- Chegada já tem data prevista, mas não hora
        3- Chegada já tem hora previsa, mas não data
        4- Chegada não tem nem hora nem data prevista
        5- Para cada caso, testar passando data e hora e sem passar data e hora (usar atual)
    """
    def test_chegada_sem_data_previsao_passando_data_chegada(self):
        """Chegada sem data de previsão, deve trazer o dia de chegada como previsão"""
        c1 = Carregamento.objects.get(nr_nota_fis='11')
        c1.set_chegada(date='2017-02-02 12:00:00', grade='22:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_saida,datetime.datetime(2017,2,2).date())

    def test_chegada_sem_data_previsao_sem_data_chegada(self):
        """Chegada sem data de previsão e sem data de chegada, deve trazer o dia atual como previsão"""
        c1 = Carregamento.objects.get(nr_nota_fis='11')
        c1.set_chegada(date=None, grade='22:00:00', placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_saida, datetime.datetime.now().date())

    def test_chegada_sem_grade(self):
        """Chegada em carregamento sem grade, deve trazer a hora de chegada como grade"""
        c1 = Carregamento.objects.get(nr_nota_fis='11')
        c1.dt_saida='2017-02-02'
        c1.set_chegada(date='2017-02-02 12:00:00', grade=None, placa='1111', lacre='1111', )
        self.assertEqual(c1.hr_grade, datetime.datetime.strptime(c1.dt_hr_chegada, "%Y-%m-%d %H:%M:%S").time())

    def test_chegada_sem_grade_sem_data(self):
        """Chegada em carregamento sem data e hora de chegada, deve trazer a hora atual como data e hora de chegada"""
        c1 = Carregamento.objects.get(nr_nota_fis='11')
        c1.set_chegada(date=None, grade=None, placa='1111', lacre='1111', )
        self.assertEqual(c1.dt_hr_chegada, datetime.datetime.now().replace(microsecond=0))
