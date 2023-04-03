from django.shortcuts import redirect, render
from .forms import DatosForm
from django.http import HttpRequest
from .models import Datos

# Create your views here.


def index(request):

    return render (request, 'home.html')


def registrarCurso(request):
    nombre= request.POST['Nombre']
    numero= request.POST['Numero']
    dni= request.POST['DNI']
    cp= request.POST['CP']
    mensaje =request.POST['Mensaje']

    datos=Datos.objects.create(nombre=nombre, numero=numero, dni=dni, cp=cp, mensaje=mensaje)

    return redirect ('/')