from django.shortcuts import render, redirect
from .forms import FormularioRegistroUsuario, FormularioRegistroEstudiante
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Usuario

def inicio(request):
    return render(request, 'usuarios/inicio.html', {})

def registro(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            cedula = form.cleaned_data.get('cedula')
            a.username = cedula
            a.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('usuarios:inicio')
    else:
        form = FormularioRegistroUsuario()

    return render(request, 'usuarios/registro.html', {'form': form})

def registro_estudiante(request):
    if request.method == 'POST':
        form = FormularioRegistroEstudiante(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('usuarios:inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('usuarios:inicio')

    context = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/consulta.html', context)
