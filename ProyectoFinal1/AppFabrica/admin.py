from django.contrib import admin

from .models import Empleado, Mayorista, Prospecto, Zapato

# Register your models here.
admin.site.register(Zapato)
admin.site.register(Empleado)
admin.site.register(Mayorista)
admin.site.register(Prospecto)