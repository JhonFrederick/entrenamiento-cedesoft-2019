from django.shortcuts import render, redirect
from .forms import FormularioRegistroUsuario
from django.contrib import messages

def inicio(request):
    return render(request, 'usuarios/inicio.html', {})

def registro(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid():
            a = form.save(commit = False)
            cedula = form.cleaned_data.get('cedula')
            a.username = cedula
            a.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('usuarios:inicio')
    else:
        form = FormularioRegistroUsuario()
    
    return render(request, 'usuarios/registro.html', {'form': form})
