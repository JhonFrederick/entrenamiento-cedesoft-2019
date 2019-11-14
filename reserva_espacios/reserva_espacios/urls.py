"""reserva_espacios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),  #<-- Solo usar para pruebas iniciales
    path('', views.login_view, name = 'login'),
    path('usuarios/', include('apps.usuarios.urls', namespace='usuarios')),
    path('espacios/', include('apps.espacios.urls', namespace='espacios')),
    path('reservas/', include('apps.reservas.urls', namespace='reservas'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
