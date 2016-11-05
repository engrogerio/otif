# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import treinamento_detail
from views import TreinamentoListView
from views import report_index
from views import TreinamentoNecessidadeDetailView
from views import TreinamentoNecessidadeListView
#from views import treinamento_table

urlpatterns = [
    url(r'^$', report_index, name='report'),
    url(r'^treinamentos_por_funcionario/(?P<id>\d+)/$', treinamento_detail, name ='treinamento_detail'),
    url(r'^treinamentos_por_funcionario/$', TreinamentoListView.as_view(), name='treinamento_list'),
    #url(r'^treinamentos_table/$', treinamento_table, name='treinamento_table'),
    url(r'^treinamentos_necessidade_por_funcionario/(?P<id>\d+)/$', TreinamentoNecessidadeDetailView.as_view(), name ='treinamento_necessidade_detail'),
    url(r'^treinamentos_necessidade_por_funcionario/$', TreinamentoNecessidadeListView.as_view(), name='treinamento_necessidade_list'),
    ]
