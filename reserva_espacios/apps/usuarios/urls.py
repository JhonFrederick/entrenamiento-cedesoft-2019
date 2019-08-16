from django.urls import path
from apps.usuarios.views import *

app_name = 'usuarios'
urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('logout/', logout_view, name = 'logout'),
    path('perfil/', perfil, name ='perfil'),
    path('editar_perfil/<str:cedula>', editarUsuario, name = 'editar'),
]
