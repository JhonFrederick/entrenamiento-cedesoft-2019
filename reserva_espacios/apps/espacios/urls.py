from django.urls import path, re_path
from .views import crearEspacio,listarEspacio,editarEspacio,eliminarEspacio

app_name = 'espacios'

urlpatterns = [
    path('crear_espacio/',crearEspacio, name = 'crear_espacio'),
    path('consultar_espacio/',listarEspacio, name = 'consultar_espacio'),
    path('editar_espacio/<int:numero>',editarEspacio, name = 'editar_espacio'),
    path('eliminarespacio/<int:id>',eliminarEspacio, name = 'eliminar_espacio')
    
]