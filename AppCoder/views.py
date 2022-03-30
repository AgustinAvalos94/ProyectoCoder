from calendar import c
from django.shortcuts import render
from django.http import HttpResponse
from models import Curso
# Create your views here.

def curso(self):
    
    curso = Curso(nombre="Desarrollo Web", camada="11111")

    curso.save()

    documento = f"El Curso es: {curso.nombre}, la camada: {curso.camada}"

    return HttpResponse(documento)