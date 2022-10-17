from django import forms
from cliente.models import Cliente, Carteira

class Formulario(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nome','sexo','nascimento','email')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control'}),
            'sexo': forms.Select(attrs={ 'class': 'form-control'}),
            'categoria': forms.Select(attrs={ 'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={ 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={ 'class': 'form-control'}),
        }


class Formulario_Carteira(forms.ModelForm):

    class Meta:
        model = Carteira
        fields = ('carteira',)

        widgets = {
            'carteira': forms.NumberInput(attrs={ 'class': 'form-control'}),
        }