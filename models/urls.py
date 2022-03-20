from django.urls import path
from . import views

urlpatterns = [
    path("comitente/crear/", views.crear_comitente, name = "crear_comitente"),
]
