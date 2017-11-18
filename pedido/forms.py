# -*- encoding=utf-8 -*-

from django import forms
from falta.models import Motivo, MotivoDeAlteracaoDaAgenda, MotivoAtraso

class UpdateDateForm(forms.Form):

    data = forms.DateTimeField(label='Data/Hora', required=False)
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    ds_placa = forms.CharField(max_length=8, required=False, label='Placa do veículo')
    nr_lacre = forms.CharField(max_length=10, required=False, label='Número de lacre')


class UpdateGradeForm(forms.Form):

    data = forms.DateTimeField(label='Data/Hora', required=False)
    grade = forms.TimeField(label='Grade(hh:mm)', required=False)
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    ds_placa = forms.CharField(max_length=8, required=False, label='Placa do veículo')
    nr_lacre = forms.CharField(max_length=10, required=False, label='Número de lacre')


class AddMotivoAtrasoCarregamentoForm(forms.Form):
    
    motivo = forms.ModelChoiceField(queryset=MotivoAtraso.objects.all())
    ds_obs = forms.CharField(max_length=500, required=False, label='Obs')
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)


class AddAgendamentoForm(forms.Form):
    
    data = forms.DateTimeField(label='Data de agendamento', required=False)
    motivo =forms.ModelChoiceField(label='Motivo da alteração', 
        queryset=MotivoDeAlteracaoDaAgenda.objects.all() , required=False)
    protocolo = forms.CharField(label='Protocolo', max_length=100, required=False)
    obs = forms.CharField(label='Obs.', max_length=200, required=False)
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
   
    def __init__(self, *args, **kwargs):
        super(AddAgendamentoForm, self).__init__( *args, **kwargs)
        self.fields['motivo'].required = False # add condition for becoming required