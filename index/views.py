from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index/index.html")

def plantilla(request):
    return render(request,"index/plantilla.html")
