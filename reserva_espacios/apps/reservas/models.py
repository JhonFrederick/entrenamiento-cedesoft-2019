from django.db import models

# Create your models here.
class Reserva(models.Model):
    id_solicitante = models.ForeignKey('usuarios.Usuario', on_delete = models.CASCADE)
    codigo_espacio = models.ForeignKey('espacios.Espacio', on_delete = models.CASCADE)
    fecha_solicitud = models.DateField(auto_now = True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    proposito = models.TextField()
    
    #ESTADO CHOICES
    EN_ESPERA = "En espera"
    ACEPTADO = "Aceptado"
    RECHAZADO = "Rechazado"

    ESTADOS_CHOICES = {
        (ACEPTADO, 'Aceptado'),
        (EN_ESPERA, 'En espera'),
        (RECHAZADO, 'Rechazado'),
    }

    estado = models.CharField(
        choices=ESTADOS_CHOICES,
        max_length=10,
        default = EN_ESPERA
    )

