from django.shortcuts import render
from .models import Mascota
from .forms import MascotaForm

# Create your views here.

def login(request):
    return render(request, 'ControlDeVeterinaria/log.html', {})

def index(request):
    return render(request, 'ControlDeVeterinaria/index.html', {})

def crearMascotas(request):
    listaMascotas = Mascota.objects.all()
    form = MascotaForm(request.POST)
    if form.is_valid():
        form.save()
    context ={
        'form':form,
        'listaMascota':listaMascotas
    }
    return render(request, 'ControlDeVeterinaria/crearMascota.html', context)
