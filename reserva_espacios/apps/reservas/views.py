from django.shortcuts import render, redirect
from .forms import FormularioRegistroReserva
from django.contrib import messages
from .models import *
from apps.espacios.models import *

# Create your views here.
def solicitar_view(request):
    if request.method == 'POST':
        form = FormularioRegistroReserva(request.POST, initial={'estado': Reserva.EN_ESPERA})
        if form.is_valid():
            f = form.save(commit=False)
            f.id_solicitante = request.user
            f.save()
            messages.success(request, "Se creo la reserva exitosamente")
            return redirect('reservas:solicitar')
    else:
        form = FormularioRegistroReserva()

    return render(request, 'reservas/solicitar.html', {'form': form})

def consultar_reservas(request, pk):
    reservas = Reserva.objects.filter(estado='Aceptado', codigo_espacio=pk)
    reservasEs = Reserva.objects.filter(estado='En espera', codigo_espacio=pk)
    esp = Espacio.objects.get(id=pk)
    titulo = esp.espacios+" "+str(esp.numero)
    return render(request, 'reservas/consultar2.html', {'reservas': reservas, 'reservasE': reservasEs, 'titulo': titulo})

def menu(request):
    espacios = Espacio.objects.filter(activo=True)
    return render(request, 'reservas/menu.html', {'espacios': espacios})

def aceptar_reserva(request, pk):
    reserva = Reserva.objects.get(id=pk)
    numero = reserva.codigo_espacio.id
    reserva.estado = "Aceptado"
    reserva.save()
    return redirect('reservas:consultar_reservas', numero)

def rechazar_reserva(request, pk):
    reserva = Reserva.objects.get(id=pk)
    numero = reserva.codigo_espacio.id
    reserva.estado = "Rechazado"
    reserva.save()
    return redirect('reservas:consultar_reservas', numero)