from django import forms
from .models import Autor

class EspacioForm(forms.ModelForm):
    class Meta:
        model = Espacio
        fields = ['numero','espacios','descripcion','imagen','edificio','capacidad','activo']