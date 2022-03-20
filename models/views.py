from django.shortcuts import render

# Create your views here.
def crear_comitente(request):
    form = None
    return render(request, "models/crear_comitente.html", {"form": form })