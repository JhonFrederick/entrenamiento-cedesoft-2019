from django.shortcuts import render, redirect
from .forms import FormularioRegistroUsuario, FormularioRegistroEstudiante
from django.contrib import messages
from .models import Usuario

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

<<<<<<< HEAD


=======
def registro_estudiante(request):
    if request.method == 'POST':
        form = FormularioRegistroEstudiante(request.POST)
        if form.is_valid():
            a = form.save(commit = False)
            cedula = form.cleaned_data.get('cedula')
            a.username = cedula
            a.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('usuarios:inicio')
    else:
        form = FormularioRegistroEstudiante()
    
    return render(request, 'usuarios/registro.html', {'form': form})

def consulta_usuario(request):

    context = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/consulta.html', context)
>>>>>>> 2d02d640c05c2a3880b2f48cd71d06fa8f666057
