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
            return redirect('usuarios:inicio') 
    else:
        espacio_form = EspacioForm()
    return render(request,'espacios/registro.html',{'espacio_form':espacio_form})


def listarEspacio(request):
    espacios = Espacio.objects.all()
    return render(request, 'espacios/listar_espacios.html',{'espacios':espacios})


        
    