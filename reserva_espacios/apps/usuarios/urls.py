from django.urls import path

from apps.usuarios.views import *

app_name = 'usuarios'
urlpatterns = [
    path('inicio/', inicio, name='inicio'),
]