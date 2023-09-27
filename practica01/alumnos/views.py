from django.shortcuts import render, redirect
from .models import Alumno

def home(request):
    alumnoListado = Alumno.objects.all()
    return render(request, "gestionAlumno.html", {"alumno": alumnoListado})

def registrarAlumno(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['numTelefono']
    email = request.POST['txtEmail']
    seccion = request.POST['txtSeccion']


    alumno = Alumno.objects.create(codigo = codigo, nombre = nombre, apellido = apellido, telefono = telefono, email = email, seccion = seccion)
    return redirect('/')
