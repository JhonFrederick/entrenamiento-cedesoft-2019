from django import forms
from .models import Espacio

class EspacioForm(forms.ModelForm):
    class Meta:
        model = Espacio
        fields = ['numero','espacios','descripcion','imagen','edificio','capacidad']