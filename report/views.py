# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from treinamento.models import Treinamento
from funcionario.models import Funcionario

from django.db.models import Sum
from django.views import generic
from django.http import Http404
import datetime


def report_index(request):
    return render(request, 'report_index.html',)


"""
Reports related to treinamento
"""

class TreinamentoListView(generic.ListView):
    template_name = 'treinamento_list.html'
    model = Funcionario

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated():
            context = super(TreinamentoListView, self).get_context_data(**kwargs)
            startdate = self.request.GET.get('start_date', '01/01/2000')
            enddate = self.request.GET.get('end_date', datetime.datetime.now().strftime("%d/%m/%Y"))
            format = '%d/%m/%Y'
            start_date = datetime.datetime.strptime(startdate, format)
            end_date = datetime.datetime.strptime(enddate, format)
            self.request.session['start_date'] = startdate
            self.request.session['end_date'] = enddate
            try:
                self.unit_name = self.request.user.user_business_unit
                total_horas_por_funcionario = Treinamento.objects.filter(business_unit__unit=self.unit_name).filter(funcionario__nome__contains = self.request.GET.get('q', '')).filter(data__range = (start_date, end_date)).values('funcionario__matricula', 'funcionario__nome', 'funcionario__id').annotate(total_horas=Sum('carga_horaria')).order_by('funcionario__nome')
                total_horas = total_horas_por_funcionario.aggregate(sum=Sum('total_horas'))['sum']
                context['start_date'] = start_date
                context['end_date'] = end_date
                context['total_horas_por_funcionario'] = total_horas_por_funcionario
                context['total_horas'] = total_horas
            except:
                Http404
            return context
        else:
            raise Http404


def treinamento_detail(request, id=None):
    if request.user.is_authenticated():
        startdate = request.session['start_date']
        enddate = request.session['end_date']
        format = '%d/%m/%Y'
        start_date = datetime.datetime.strptime(startdate, format)
        end_date = datetime.datetime.strptime(enddate, format)
        queryset = Treinamento.objects.filter(funcionario=id).filter(data__range = (start_date, end_date)).order_by('data')
        total_horas = Treinamento.objects.filter(funcionario=id).filter(data__range = (start_date, end_date)).aggregate(sum=Sum('carga_horaria'))['sum']
        funcionario = get_object_or_404(Funcionario, id=id)
        context = {
            "funcionario": funcionario,
            "treinamento_list": queryset,
            "total_horas": total_horas or 0
        }
        return render(request, "treinamento_detail.html", context)
    else:
        raise Http404


from documento.models import Documento



class TreinamentoNecessidadeListView(generic.ListView):
    template_name = 'treinamento_necessidade_list.html'
    model = Documento

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated():
            context = super(TreinamentoNecessidadeListView, self).get_context_data(**kwargs)


            self.unit_name = self.request.user.user_business_unit
            #treinamentos_realizados = Treinamento.objects.filter(business_unit__unit=self.unit_name).filter(funcionario__ativo=1).values('funcionario__matricula', 'funcionario__nome', 'funcionario__data_contratacao').order_by('funcionario__nome')
            treinamentos_pendentes = Documento.objects.filter(business_unit__unit=self.unit_name).values('cargo__id', 'cargo__cargo','id','titulo',).all().order_by('cargo__cargo')
            funcionarios_treinamentos_pendentes = Funcionario.objects.filter(business_unit__unit=self.unit_name).filter(ativo= True).values ('nome', 'cargo__cargo').filter(cargo=1) #.select_related()
            print(funcionarios_treinamentos_pendentes)
            context['treinamentos'] = treinamentos_pendentes

            return context
        else:
            raise Http404


class TreinamentoNecessidadeDetailView(generic.DetailView):
    template_name = 'treinamento_list.html'
    model = Funcionario

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated():
            context = super(TreinamentoListView, self).get_context_data(**kwargs)
            startdate = self.request.GET.get('start_date', '01/01/2000')
            enddate = self.request.GET.get('end_date', datetime.datetime.now().strftime("%d/%m/%Y"))
            format = '%d/%m/%Y'
            start_date = datetime.datetime.strptime(startdate, format)
            end_date = datetime.datetime.strptime(enddate, format)
            self.request.session['start_date'] = startdate
            self.request.session['end_date'] = enddate
            try:
                self.unit_name = self.request.user.user_business_unit
                total_horas_por_funcionario = Treinamento.objects.filter(business_unit__unit=self.unit_name).filter(funcionario__nome__contains = self.request.GET.get('q', '')).filter(data__range = (start_date, end_date)).values('funcionario__matricula', 'funcionario__nome', 'funcionario__id').annotate(total_horas=Sum('carga_horaria')).order_by('funcionario__nome')
                total_horas = total_horas_por_funcionario.aggregate(sum=Sum('total_horas'))['sum']
                context['start_date'] = start_date
                context['end_date'] = end_date
                context['total_horas_por_funcionario'] = total_horas_por_funcionario
                context['total_horas'] = total_horas
            except:
                Http404
            return context
        else:
            raise Http404

"""
# Tables2
from django.shortcuts import render
from tables import TreinamentoNecessidadeTable
from django_tables2 import RequestConfig

def treinamento_table(request):
    table = TreinamentoNecessidadeTable(Treinamento.objects.all()) #.values('business_unit_id', 'business_unit', 'codigo', 'titulo', 'business_unit_id', 'cargo__cargo',).order_by('codigo',))
    RequestConfig(request).configure(table)
    return render(request, 'treinamento_necessidade_table.html', {'table':table})
        #'table1':Documento.objects.all().values('business_unit_id', 'business_unit', 'codigo', 'titulo',) #.values('funcionario__matricula', 'funcionario__nome', 'funcionario__data_contratacao',) # 'funcionario__cargo', 'documento__codigo', 'documento__titulo','data', 'carga_horaria','validade_meses',)
        #,'table2':Documento.objects.values('business_unit_id', 'business_unit', 'codigo', 'titulo', 'business_unit_id', 'cargo__cargo',).order_by('codigo',)
"""