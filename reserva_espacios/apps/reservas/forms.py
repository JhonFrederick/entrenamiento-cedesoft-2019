from django import forms
from .models import Reserva

class FormularioRegistroReserva(forms.ModelForm):
    class Meta():
        model = Reserva
        fields = ('codigo_espacio', 'fecha_inicio', 'fecha_fin', 'hora_inicio', 'hora_fin', 'proposito')
        