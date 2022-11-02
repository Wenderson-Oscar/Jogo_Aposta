from django import forms
from cliente.models import Cliente, Carteira, JogoBicho
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username']


class Formulario(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('nome','sexo','nascimento','email')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control'}),
            'sexo': forms.Select(attrs={ 'class': 'form-control'}),
            'nascimento': forms.TextInput(attrs={ 'class': 'form-control','type':'date'}),
            'email': forms.EmailInput(attrs={ 'class': 'form-control'}),
        }


class Formulario_Carteira(forms.ModelForm):

    class Meta:
        model = Carteira
        fields = ('n_conta','carteira')

        widgets = {
            'n_conta': forms.TextInput(attrs={ 'class': 'form-control'}),
            'carteira': forms.NumberInput(attrs={ 'class': 'form-control'}),
        }


class EscolhaBicho(forms.ModelForm):

    class Meta:
        model = JogoBicho
        fields = ('bichos',)

        widgets = {
            'bichos': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }