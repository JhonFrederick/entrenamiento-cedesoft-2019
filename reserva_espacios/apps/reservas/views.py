from django.shortcuts import render, redirect
from .forms import FormularioRegistroReserva
from django.contrib import messages


# Create your views here.
def solicitar_reserva_view(request):
    if request.method == 'POST':
        form = FormularioRegistroReserva(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Se creo la reserva exitosamente")
            return redirect('reservas:solicitar_reserva')

    else:
        form = FormularioRegistroReserva()

    return render(request, 'reservas/solicitar.html', {'form': form})
