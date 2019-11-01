from django.db import models

# Create your models here.
class Espacio(models.Model):
    numero = models.CharField(max_length = 4)
    
    #TIPO ESPACIO CHOICES
    SALON = 'Salon'
    AUDITORIO = 'Auditorio'
    SALA_DE_COMPUTO = 'Sala de computo'
    SALA_DE_REUNIONES = 'Sala de reuniones'

    ESPACIOS_CHOICES={
        (SALON, 'salon'),
        (AUDITORIO, 'auditorio'),
        (SALA_DE_COMPUTO, 'sala_de_computo'),
        (SALA_DE_REUNIONES, 'sala_de_reuniones'),
    }

    espacios = models.CharField(
        choices = ESPACIOS_CHOICES,
        max_length = 30,
        default = SALON
    )

    descripcion = models.TextField()
    imagen = models.ImageField(upload_to = 'fotos_espacios')
    edificio = models.CharField(max_length = 10)
    capacidad = models.IntegerField()
    activo = models.BooleanField(default = True)

    def __str__(self):
        return self.espacios + " " + self.numero

    class Meta:
        unique_together = ('numero', 'espacios',)