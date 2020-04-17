
from .models import Wackywidgets
from django import forms
from django.forms import ModelForm


class WackywidgetsForm(ModelForm):
    class Meta:
        model = Wackywidgets
        fields = ['description', 'quantity']
