from django import forms

class comitenteformulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    nacimiento = forms.DateTimeField()
    nrocomitente = forms.IntegerField()
    perfilriesgo = forms.CharField(max_length=20)
    