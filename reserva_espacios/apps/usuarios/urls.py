from django.urls import path
from apps.usuarios.views import *

app_name = 'usuarios'
urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
]
