from multiprocessing.spawn import import_main_path
from django.contrib import admin
from AppFabrica import views
from .views import buscar, sobre_mi, buscar_zapato, detalle_zapato, editar_usuario, loginview, registrar, lista_zapatos, editar_zapato, eliminar_zapato, crear_zapato, crear_empleado, form_mayorista, inicio, suscriptores
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path ('', inicio, name= "inicio"),
    path ('empleados/', crear_empleado),
    path ('crearzapato/', crear_zapato, name= "crearzapato"),
    path ('compra-mayoristas/', form_mayorista, name= "form_mayorista"),
    path ('suscriptores/', suscriptores, name= "suscriptores"),
    path ('buscarzapato/', buscar_zapato, name= "buscar_zapato"),
    path ('buscar/', buscar , name= "buscar"),
    path ('zapatos/', lista_zapatos , name= "lista_zapatos"),
    path ('editarzapato/<int:id>', editar_zapato , name= "editar_zapato"),
    path ('eliminarzapato/<int:id>', eliminar_zapato, name= "eliminar_zapato"),
    path ('login/', loginview, name= "login"),
    path ('registrar/', registrar, name= "registrar"),
    path ('logout/', LogoutView.as_view(template_name="logout.html"), name= "logout"),
    path ('editarusuario/', editar_usuario, name= "editar_usuario"),
    path ('detallezapato/<pk>', detalle_zapato.as_view(), name= "detallezapato"),
    path ('sobremi', sobre_mi, name= "sobremi"),
    path ('verzapato/<id>', lista_zapatos, name= "ver_zapato"),
]

