from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateTimeField()
    nrocomitente = models.IntegerField()
    perfilriesgo = models.CharField(max_length=20)

class Broker(models.Model):
    broker = models.CharField(max_length=20)
    activo = models.CharField(max_length=40)
    montoinicial = models.IntegerField()   

class Banco(models.Model):
    Banco = models.CharField(max_length=40)
    Nrocuenta = models.IntegerField()
    Moneda = models.CharField(max_length=10)
    
