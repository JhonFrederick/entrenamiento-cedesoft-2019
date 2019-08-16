from django.urls import path
from .views import *
app_name = 'reservas'

urlpatterns = [
    path('solicitar_reserva/', solicitar_reserva_view, name = "solicitar_reserva"),
]