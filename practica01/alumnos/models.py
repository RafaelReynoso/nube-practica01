from django.db import models

# Create your models here.

class Alumno(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    seccion = models.CharField(max_length=15)