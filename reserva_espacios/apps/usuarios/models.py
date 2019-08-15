from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.get_full_name()

    cedula = models.CharField(primary_key=True, max_length=10)

    #SEDES CHOICES
    MELENDEZ = 'melendez'
    SAN_FERNANDO = 'san_fernando'
    ZARZAL = 'zarzal'
    TULUA = 'tulua'

    SEDES_CHOICES={
        (MELENDEZ, 'Melendez'),
        (SAN_FERNANDO, 'San Fernando'),
        (ZARZAL, 'Zarzal'),
        (TULUA, 'Tulua'),
    }

    sede = models.CharField(
        choices = SEDES_CHOICES,
        max_length = 15,
        default = MELENDEZ
    )

    #DEPENDENCIA CHOICES
    ESC_ING_SISTEMAS = 'esc_ing_sistema'

    DEPENDENCIA_CHOICES={
        (ESC_ING_SISTEMAS, 'Escuela de Ingenieria de Sistemas'),
    }

    dependencia = models.CharField(
        choices = DEPENDENCIA_CHOICES,
        max_length=50,
        default = ESC_ING_SISTEMAS
    )

    #ROL CHOICES
    ESTUDIANTE = 'estudiante'
    DOCENTE = 'docente'
    DIRECTOR = 'director'
    ADMINISTRADOR = 'administrador'

    ROL_CHOICES = {
        (ESTUDIANTE, 'Estudiante'),
        (DOCENTE, 'Docente'),
        (DIRECTOR, 'Director'),
        (ADMINISTRADOR, 'Administrador'),
    }

    rol = models.CharField(
        choices = ROL_CHOICES,
        max_length = 40,
        default = ESTUDIANTE    
    )

    foto_perfil = models.ImageField(default = 'default.png', upload_to='fotos_perfil')


class Estudiante(Usuario):
    codigo = models.CharField(max_length=7, unique=True)
    monitor = models.BooleanField(default = False)


