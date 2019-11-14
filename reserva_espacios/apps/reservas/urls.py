from django.urls import path
from .views import *
app_name = 'reservas'

urlpatterns = [
    path('solicitar/', solicitar_view, name = "solicitar"),
    path('consultar/<int:pk>/', consultar_reservas, name = "consultar_reservas"),
    path('aceptar/<int:pk>/', aceptar_reserva, name = "aceptar_reserva"),
    path('rechazar/<int:pk>/', rechazar_reserva, name = "rechazar_reserva"),
    path('menu/', menu, name = "menu"),
]
