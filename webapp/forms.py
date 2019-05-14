from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CalcModel

class RegUser(UserCreationForm):
    email = forms.EmailField(required=True)

class CalcForm(forms.ModelForm):
    class Meta:
        model = CalcModel
        fields = ['out', 'to']

        widgets = {
            'out': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'name': 'out'}),
            'to': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'name': 'to'})
        }