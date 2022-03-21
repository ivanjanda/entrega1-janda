from django.shortcuts import render
from .forms import comitenteformulario, bancoformulario, brokerformulario
from .models import Persona

def crear_comitente(request):
    if request.method == "POST":
        form = comitenteformulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            persona = Persona(nombre=data["nombre"], apellido=data["apellido"], nacimiento=data["nacimiento"], nrocomitente=data["nrocomitente"], perfilriesgo=data["perfilriesgo"])
            persona.save()
            return render(request, "index/index.html",{})
        
    return render(request, "models/crear_comitente.html", {"form": form })

def crear_banco(request):
    form = bancoformulario()
    return render (request, "models/crear_banco.html", {"form": form })

def crear_banco(request):
    form = brokerformulario()
    return render (request, "models/crear_broker.html", {"form": form })