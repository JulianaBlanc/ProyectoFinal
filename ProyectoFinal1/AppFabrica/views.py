import email
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context, Template, loader
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import FormProspecto, MayoristaFormulario, ZapatoFormulario, UserRegisterForm, UserEditForm
from .models import Empleado, Mayorista, Prospecto, Zapato, Avatar
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio (request):
    try:
        avatar = Avatar.objects.get(user=request.user)
        return render(request, "inicio.html", {'url': avatar.imagen.url})
    except:
        return render(request, "inicio.html")



def crear_zapato (request):
    if request.method == 'POST':
        form_zapato = ZapatoFormulario(request.POST)
        if form_zapato.is_valid():
            print('error1')
            data=form_zapato.cleaned_data
            zapato = Zapato (
                nombre=data['nombre'], 
                material=data['material'],
                color=data['color'], 
                talle=data['talle'],
                stock=data['stock'],
                precio=data['precio'],
                foto=data['foto']
            )
            print('error1')
            zapato.save()
            return HttpResponseRedirect ('/AppFabrica/zapatos')
    else:
        form_zapato = ZapatoFormulario()
        return render (request, "crearcalzado.html", {"form_zapato": form_zapato})

def lista_zapatos (request):
    zapatos = Zapato.objects.all()
    return render (request, "listazapatos.html", {"zapatos": zapatos})

def eliminar_zapato (request, id):
    if request.method == 'POST':
        zapato = Zapato.objects.get(id=id)
        zapato.delete()
        zapatos = Zapato.objects.all()
        return render (request, "listazapatos.html", {"zapatos":zapatos})

def editar_zapato (request, id):
    zapato = Zapato.objects.get(id=id)
    if request.method == 'POST':
        form_zapato = ZapatoFormulario(request.POST, files=request.FILES)
        print('hola1')
        if form_zapato.is_valid():
            data=form_zapato.cleaned_data
            zapato.nombre=data['nombre']
            zapato.material=data['material']
            zapato.color=data['color']
            zapato.talle=data['talle']
            zapato.stock=data['stock']
            zapato.precio=data['precio']
            zapato.foto=data['foto']
            zapato.save()
        print(form_zapato.errors)
        return HttpResponseRedirect('/AppFabrica/zapatos')
    else:
        form_zapato = ZapatoFormulario (initial={
            "nombre": zapato.nombre,
            "material":zapato.material, 
            "color":zapato.color, 
            "talle":zapato.talle,
            "stock":zapato.stock,
            "precio":zapato.precio,
            "foto":zapato.foto
        })
    return render (request, "editarcalzado.html", {"form_zapato":form_zapato, "id":id , "url":zapato.foto.url})


def crear_empleado (request, nombre, apellido, legajo):
    empleado = Empleado (nombre=nombre, apellido=apellido, legajo=legajo)
    empleado.save()

def crear_mayorista(request, nombre, apellido, email, telefono):
    mayorista = Mayorista(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
    mayorista.save()
    return render (request, "crearmayorista.html")
    
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
        return render (request, "crearmayoristas.html", {"form_mayorista": form_mayorista})

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
    return render (request, "descripcion_zapato.html", {'zapato': zapato, 'nombre': modelo_buscado})

def loginview (request): 
    if request.method == 'POST': 
        form_login = AuthenticationForm(request, data=request.POST) 
        if form_login.is_valid(): 
            data=form_login.cleaned_data 
            usuario=data['username'] 
            contrasena=data['password']
            user=authenticate(username=usuario, password=contrasena) 
            if user: 
                login(request, user) 
                return render (request, "inicio.html", {'mensaje': f'Bienvenido {usuario}'}) 
            else: 
                return render (request, "inicio.html", {'mensaje': f'Error en los datos'}) 
        return render (request, "inicio.html", {'mensaje': f'Usuario'})
    else: 
        form_login = AuthenticationForm() 
        return render (request, "login.html", {'form_login': form_login})


def registrar(request):
    if request.method == 'POST':
        registro_usuario = UserRegisterForm(request.POST)
        if registro_usuario.is_valid():
            username=registro_usuario.cleaned_data['username']
            registro_usuario.save()
            return render (request, "inicio.html", {'mensaje': f'Usuario {username} creado con éxito'}) 
        else:
            registro_usuario= UserRegisterForm()
            return render (request, "inicio.html", {'mensaje': f'Error al crear usuario: {registro_usuario.errors}'}) 
    else:
        registro_usuario= UserRegisterForm()
        return render (request, "registro.html", {'registro_usuario': registro_usuario}) 

def editar_usuario(request):
    usuario= request.user
    if request.method == "POST":
        form_editar_usuario=UserEditForm(request.POST)
        if form_editar_usuario.is_valid():
            data=form_editar_usuario.cleaned_data
            usuario.first_name=data['first_name']
            usuario.last_name=data['last_name']
            usuario.email=data['email']
            usuario.save()
            return render (request, "inicio.html", {'mensaje': f'Datos actualizados!'}) 
        return render (request, "inicio.html", {'mensaje': f'Las contraseñas no coinciden!'})  
    else:
        form_editar_usuario = UserEditForm(instance=request.user)
        return render (request, "editarusuario.html", {"form_editar_usuario": form_editar_usuario})
