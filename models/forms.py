from django import forms

class comitenteformulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    nacimiento = forms.DateTimeField()
    nrocomitente = forms.IntegerField()
    perfilriesgo = forms.CharField(max_length=20)

class brokerformulario(forms.Model):
    broker = forms.CharField(max_length=20)
    activo = forms.CharField(max_length=40)
    montoinicial = forms.IntegerField()   

class bancoformulario(forms.Model):
    Banco = forms.CharField(max_length=40)
    Nrocuenta = forms.IntegerField()
    Moneda = forms.CharField(max_length=10)    