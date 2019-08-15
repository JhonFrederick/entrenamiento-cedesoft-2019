from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class FormularioRegistroUsuario(UserCreationForm):
    cedula = forms.CharField()
    
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'cedula', 'sede', 'dependencia', 'rol')

