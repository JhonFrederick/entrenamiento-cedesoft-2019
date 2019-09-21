from django.urls import path
from .views import *
app_name = 'reservas'

urlpatterns = [
    path('solicitar/', solicitar_view, name = "solicitar"),
    path('consultar/', consultar_reservas, name = "consultar_reservas"),
    path('aceptar/<int:pk>/', aceptar_reserva, name = "aceptar_reserva"),
    path('consultar/<int:pk>/', rechazar_reserva, name = "rechazar_reserva"),
]