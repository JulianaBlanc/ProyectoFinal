import email
from turtle import color
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Zapato (models.Model):
    nombre = models.CharField(max_length=50, default=None)
    material = models.CharField(max_length=50, default=None)
    color = models.CharField(max_length=50, default=None)
    talle = models.IntegerField(default=None)
    stock = models.IntegerField(default=None)
    precio = models.FloatField(default=None)

    def __str__(self):
        return f' {self.nombre} - {self.material} - {self.color} - {self.talle} - {self.stock} - {self.precio}'


class Empleado (models.Model):
    nombre = models.CharField(max_length=50, default=None)
    apellido = models.CharField(max_length=50, default=None)
    legajo = models.IntegerField(default=None)

class Mayorista (models.Model):
    nombre = models.CharField(max_length=50, default=None)
    apellido = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    telefono = models.IntegerField(default=None)
    def __str__(self):
        return f' {self.nombre} - {self.apellido} - {self.email} - {self.telefono}'

class Prospecto (models.Model):
    email = models.EmailField(default=None)
    def __str__(self):
        return f' {self.email}'

class Avatar (models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)



