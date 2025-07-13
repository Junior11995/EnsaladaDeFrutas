# Create your models here.
from django.db import models

class Fruta(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    fruta = models.ForeignKey(Fruta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
