from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView,
    CreateView
 ) #importacion de vistas genericas
#todas las vistas genericas necesitaran un template(archivo.html) para trabajar
from .models import Prueba
from .forms import PruebaForm

class pruebaView(TemplateView):
    template_name = 'home/prueba.html' #indico donde se encuentra el template con /


class ResumeFoundation(TemplateView):
    template_name = 'home/resume_foundation.html'



class pruebalistView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaStrings' #crea una varialbe para mostrar el queryset
    queryset = ['2','hello','savage','3'] # queryset hace referencia a la listas  del view

class listaprueba(ListView):
    template_name = 'home/lista2.html'
    model = Prueba
    context_object_name = 'lista'


class insertaregistro(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm #va a ser igual form ubicado en forms
    success_url = '/'

class frem(TemplateView):
    template_name = 'home/framwork.html'