# -*- encoding=utf-8 -*-

from django import forms
from falta.models import Motivo

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


class AddMotivoCarregamentoForm(forms.Form):
    
    motivo = forms.ModelChoiceField(queryset=Motivo.objects.all())
    ds_obs = forms.CharField(max_length=500, required=False, label='Obs')
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)