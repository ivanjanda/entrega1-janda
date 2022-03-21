from django.urls import path
from . import views

urlpatterns = [
    path("comitente/crear/", views.crear_comitente, name = "crear_comitente"),
    path("broker/crear/", views.crear_broker, name = "crear_broker"),
    path("banco/añadir/", views.crear_banco, name = "crear_banco"),
    
]
