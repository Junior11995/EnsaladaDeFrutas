from django import forms
from .models import Fruta, Usuario

class FrutaForm(forms.ModelForm):
    class Meta:
        model = Fruta
        fields = ['nombre', 'color', 'tipo', 'descripcion']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'fruta']
