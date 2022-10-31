from django import forms

class MayoristaFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()

class ZapatoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    material = forms.CharField(max_length=50)
    color = forms.CharField(max_length=50)
    talle = forms.IntegerField()
    stock = forms.IntegerField()
    precio = forms.FloatField()

class FormProspecto(forms.Form):
    email = forms.EmailField()
