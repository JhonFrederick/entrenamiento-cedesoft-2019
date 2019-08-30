from django.shortcuts import render, redirect
from .forms import FormularioRegistroReserva
from django.contrib import messages
from .models import Reserva


# Create your views here.
def solicitar_view(request):
    if request.method == 'POST':
        form = FormularioRegistroReserva(request.POST, initial={'estado': Reserva.EN_ESPERA})
        if form.is_valid():
            form.save()
            messages.success(request, "Se creo la reserva exitosamente")
            return redirect('reservas:solicitar')
    else:
        form = FormularioRegistroReserva()

    return render(request, 'reservas/solicitar.html', {'form': form})
