from django import forms
from .models import Reserva

class FormularioRegistroReserva(forms.ModelForm):
    class Meta():
        model = Reserva
        fields = ('id', 'codigo_espacio', 'fecha_inicio', 'fecha_fin', 'hora_inicio', 'hora_fin', 'proposito', 'estado')
        