from django.urls import path
from apps.usuarios.views import *

app_name = 'usuarios'
urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('registro/estudiante', registro_estudiante, name='registro_estudiante'),
    path('consulta', consulta_usuario, name='consulta_u'),
]
