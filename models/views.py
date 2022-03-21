from django.shortcuts import render
from .forms import comitenteformulario

def crear_comitente(request):
    form = comitenteformulario()
    return render(request, "models/crear_comitente.html", {"form": form })