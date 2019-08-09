from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import EspacioForm
from .models import Espacio

# Create your views here.


def crearEspacio(request):
    if request.method =='POST':
        espacio_form = EspacioForm(request.POST)
        if espacio_form.is_valid():
            espacio_form.save()
            return redirect('index') 
    else:
        espacio_form = EspacioForm()
        
    #return render(request,'espacios/crear_espacio.html',{'espacio_form':EspacioForm})