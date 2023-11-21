from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.

def crear_curso(request):
    curso = Curso(nombre ="Python", camada=47785)
    curso.save()
    
    return HttpResponse(f"su curso es {curso.nombre} y la camada es {curso.camada}")

