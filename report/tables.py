import django_tables2 as tables
from treinamento.models import Treinamento
from documento.models import Documento

class TreinamentoRealizadoTable(tables.Table):
    class Meta:
        model = Treinamento
        attrs = {'class': 'paleblue'}
        exclude = (
            'id',
            'business_unit',
            'carga_horaria',
            'somente_cargo',
            'verificacao_eficaz',
            'verificacao_data',
            'verificacao_nome',
            'verificacao_tipo',
            'treinador',
            'docfile',
        )


class TreinamentoNecessidadeTable(tables.Table):
    class Meta:
        model = Treinamento
        attrs = {'class': 'paleblue'}
        exclude = (
            'id',
            'business_unit',
            'carga_horaria',
            'somente_cargo',
            'verificacao_eficaz',
            'verificacao_data',
            'verificacao_nome',
            'verificacao_tipo',
            'treinador',
            'docfile',
        )