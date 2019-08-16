from django import forms
from .models import Reserva

class FormularioRegistroReserva(forms.Form):
    class Meta():
        model = Reserva
        fields = ('id', 'id_solicitante', 'codigo_espacio', 'fecha_solicitud', 'fecha_inicio', 'fecha_fin', 'hora_inicio', 'hora_fin', 'proposito', 'estado')
        