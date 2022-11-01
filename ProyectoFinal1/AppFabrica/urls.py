from multiprocessing.spawn import import_main_path
from django.contrib import admin
from AppFabrica import views
from .views import buscar, buscar_zapato, crear_mayorista, crear_zapato, crear_empleado, form_mayorista, inicio, form_mayorista, suscriptores
from django.urls import path


urlpatterns = [
    path ('', inicio, name= "inicio"),
    path ('empleados/', crear_empleado),
    path ('zapatos/', crear_zapato, name= "crearzapato"),
    path ('mayoristas/', form_mayorista, name= "form_mayorista"),
    path ('suscriptores/', suscriptores, name= "suscriptores"),
    path ('buscarzapato/', buscar_zapato, name= "buscar_zapato"),
    path ('buscar/', buscar , name= "buscar"),
]