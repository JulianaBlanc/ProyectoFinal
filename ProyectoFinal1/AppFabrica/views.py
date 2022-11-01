import email
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context, Template, loader

from .forms import FormProspecto, MayoristaFormulario, ZapatoFormulario
from .models import Empleado, Mayorista, Prospecto, Zapato

# Create your views here.
def inicio (request):
    return render (request, "inicio.html")

def crear_zapato (request):
    if request.method == 'POST':
        form_zapato = ZapatoFormulario(request.POST)
        if form_zapato.is_valid():
            data=form_zapato.cleaned_data
            zapato = Zapato (
                nombre=data['nombre'], 
                material=data['material'], 
                color=data['color'], 
                talle=data['talle'],
                stock=data['stock'],
                precio=data['precio']
            )
            zapato.save()
            return HttpResponseRedirect ('/AppFabrica/')
    else:
        form_zapato = ZapatoFormulario()
        return render (request, "crearcalzado.html", {"form_zapato": form_zapato})

def ver_zapatos (request):
    zapatos = Zapato.objects.all()

def crear_empleado (request, nombre, apellido, legajo):
    empleado = Empleado (nombre=nombre, apellido=apellido, legajo=legajo)
    empleado.save()

def crear_mayorista(request, nombre, apellido, email, telefono):
    mayorista = Mayorista(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
    mayorista.save()
    return render (request, "listamayorista.html")
    

def form_mayorista(request):
    if request.method == 'POST':
        form_mayorista = MayoristaFormulario(request.POST)
        if form_mayorista.is_valid():
            data=form_mayorista.cleaned_data
            mayorista = Mayorista(
                nombre=data['nombre'], 
                apellido=data['apellido'], 
                email=data['email'], 
                telefono=data['telefono']
            )
            mayorista.save()
            return HttpResponseRedirect ('/AppFabrica/')
    else:
        form_mayorista = MayoristaFormulario()
        return render (request, "mayoristas.html", {"form_mayorista": form_mayorista})

def suscriptores(request):
    if request.method == 'POST':
        form_prospecto = FormProspecto(request.POST)
        if form_prospecto.is_valid():
            data=form_prospecto.cleaned_data
            prospecto = Prospecto(email=data['email'])
            prospecto.save()
            return HttpResponseRedirect ('/AppFabrica/')
    else:
        form_prospecto = FormProspecto()
        return render (request, "crearsuscriptor.html", {"form_prospecto": form_prospecto})

def buscar_zapato(request):
    return render (request, "buscarzapato.html")

def buscar(request):
    modelo_buscado = request.GET ['modelo']
    zapato = Zapato.objects.get(nombre=modelo_buscado)
    print(zapato.material)
    return render (request, "busquedas_modelos.html", {'zapato': zapato, 'nombre': modelo_buscado})