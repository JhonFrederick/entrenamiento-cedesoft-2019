from django.shortcuts import render, redirect
from .forms import FormularioRegistroUsuario,FormularioModificarUsuario
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Usuario
from django.core.exceptions import ObjectDoesNotExist


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
            return redirect('login')
    else:
        form = FormularioRegistroUsuario()
    
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('usuarios:inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

def perfil(request):
    return render(request, 'usuarios/perfil.html')

def editarUsuario(request, cedula):
    usuarios_form = None
    error = None
    try:
        usuario = Usuario.objects.get(cedula = cedula)
        if request.method == 'GET':
            usuarios_form = FormularioModificarUsuario(instance = usuario)
        else:
            usuarios_form = FormularioModificarUsuario(request.POST, instance = usuario)
            if usuarios_form.is_valid():
                usuarios_form.save()
            return redirect('usuarios:perfil')
    except ObjectDoesNotExist as e:
        error = e 
    
    return render (request,'usuarios/modificar.html',{'usuarios_form':usuarios_form, 'error':error})


