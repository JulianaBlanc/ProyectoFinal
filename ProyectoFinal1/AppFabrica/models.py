import email
from turtle import color
from django.db import models

# Create your models here.

class Zapato (models.Model):
    nombre = models.CharField(max_length=50, default=None)
    material = models.CharField(max_length=50, default=None)
    color = models.CharField(max_length=50, default=None)
    talle = models.IntegerField(default=None)
    stock = models.IntegerField(default=None)
    precio = models.FloatField(default=None)

class Empleado (models.Model):
    nombre = models.CharField(max_length=50, default=None)
    apellido = models.CharField(max_length=50, default=None)
    legajo = models.IntegerField(default=None)

class Mayorista (models.Model):
    nombre = models.CharField(max_length=50, default=None)
    apellido = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    telefono = models.IntegerField(default=None)

class Prospecto (models.Model):
    email = models.EmailField(default=None)



