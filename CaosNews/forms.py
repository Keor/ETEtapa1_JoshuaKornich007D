from django import forms
from django.forms import ModelForm,widgets
from .models import Colaborador

class ColaboradorForm(ModelForm):

    class Meta: 
        model = Colaborador
        fields = ['rut','foto','nomCompleto','fono','direccion','mail','pais','contrasena']

        labels ={'rut': 'Rut: ', 'foto': 'Foto: ', 'nomCompleto': 'Nombre Completo: ', 
        'fono': 'Teléfono: ','direccion': 'Dirección: ','mail': 'E-Mail: ','pais': 'País: ',
        'contrasena':'Contraseña: ',}

        widgets={
        'rut': forms.TextInput(attrs={'class': 'form-control', 'id': 'rut','name': 'rut'}), 
        'foto': forms.ClearableFileInput(attrs={'class': 'form-control','id': 'foto','name': 'foto','accept':"imagen/*"}), 
        'nomCompleto': forms.TextInput(attrs={'class': 'form-control', 'id': 'nomCompleto','name': 'nomCompleto'}), 
        'fono': forms.TextInput(attrs={'class': 'form-control','id': 'fono','name': 'fono'}),
        'direccion': forms.TextInput(attrs={'class': 'form-control', 'id': 'direccion','name': 'direccion'}), 
        'mail': forms.TextInput(attrs={'class': 'form-control', 'id': 'mail','name': 'mail'}), 
        'pais': forms.TextInput(attrs={'class': 'form-control' , 'id': 'pais','name': 'detalle'}),
        'contrasena': forms.TextInput(attrs={'class': 'form-control' , 'id': 'contrasena','name': 'contrasena'}),
        }