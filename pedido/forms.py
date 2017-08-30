# -*- encoding=utf-8 -*-

from django import forms


class UpdateDateForm(forms.Form):

    data = forms.DateTimeField(label='Data / Hora', required=False)
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    ds_placa = forms.CharField(max_length=8, required=False, label='Placa do veículo')
    nr_lacre = forms.CharField(max_length=10, required=False, label='Número de lacre')
