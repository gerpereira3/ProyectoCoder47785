
from django.contrib import admin
from django.urls import path
from AppCoder.views import busqueda_camada, crear_curso, crear_curso_form, show_html, mostrar_curso  

urlpatterns = [
    
    path('buscar/', busqueda_camada),
    path('curso/', crear_curso_form),
    path('agregar_curso/', crear_curso),
    path('show/', show_html),
    path('cursos/', mostrar_curso),
]
