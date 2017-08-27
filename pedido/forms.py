from django import forms
from datetime import datetime


class UpdateDateForm(forms.Form):
    data = forms.DateTimeField(initial=datetime.now(), required=False) #input_formats=['%Y-%m-%d %H:%M'], initial=datetime.now)
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)