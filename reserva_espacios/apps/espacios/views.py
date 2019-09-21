from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import EspacioForm
from .models import Espacio

# Create your views here.


def crearEspacio(request):
    if request.method =='POST':
        espacio_form = EspacioForm(request.POST,request.FILES)
        if espacio_form.is_valid():
            espacio_form.save()
            return redirect('espacios:consultar_espacio') 
    else:
        espacio_form = EspacioForm()
    return render(request,'espacios/registro.html',{'espacio_form':espacio_form})


def listarEspacio(request):
    espacios = Espacio.objects.all()
    return render(request, 'espacios/consultar_espacios.html',{'espacios':espacios})


def editarEspacio(request,numero):
    espacio_form = None
    error = None
    try:
        espacio = Espacio.objects.get(numero = numero)
        if request.method == 'GET':
            espacio_form = EspacioForm(instance = espacio)
        else:
            espacio_form = EspacioForm(request.POST, instance = espacio)
            if espacio_form.is_valid():
                espacio_form.save()
            return redirect('espacios:consultar_espacio')
    except ObjectDoesNotExist as e:
        error = e 
    
    return render (request,'espacios/registro.html',{'espacio_form':espacio_form, 'error':error})

    
def eliminarEspacio(request,id):
    espacio = Espacio.objects.get(numero = id)
    if request.method == 'POST':
        espacio.delete()
        return redirect('espacios:consultar_espacio')
    return render(request,'espacios/eliminar_espacios.html',{'espacio':espacio})
        
