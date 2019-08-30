from django.shortcuts import render, redirect
from .forms import FormularioRegistroReserva
from django.contrib import messages
from .models import *


# Create your views here.
def solicitar_view(request):
    if request.method == 'POST':
        form = FormularioRegistroReserva(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.id_solicitante = request.user
            f.save()
            messages.success(request, "Se creo la reserva exitosamente")
            return redirect('reservas:solicitar')
    else:
        form = FormularioRegistroReserva()

    return render(request, 'reservas/solicitar.html', {'form': form})

def consultar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/consultar.html', {'reservas': reservas})

def aceptar_reserva(request, pk):
    reserva = Reserva.objects.get(id=pk)
    reserva.estado = "Aceptado"
    reserva.save()
    return redirect('reservas:consultar_reservas')

def rechazar_reserva(request, pk):
    reserva = Reserva.objects.get(id=pk)
    reserva.estado = "Rechazado"
    reserva.save()
    return redirect('reservas:consultar_reservas')