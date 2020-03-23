from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy #para las reiderecciones de urls
# Create your views here.
from .models import Empleado #la vista va a trabajar con la db por eso importamos el modelo de empleado
#forms
from .forms import EmpleadoForm

class InicioView(TemplateView): #vista de inicio pag
    template_name = 'inicio.html' 

class listallempleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 6
    ordering = '-pk'
    context_object_name = 'empleados'
    model = Empleado
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        query = Empleado.objects.filter(first_name__icontains=palabra_clave)#nos va a retornar todo porque teiene vacio, propiedad del icontains
        return query

"""

class listallempleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4 #mostrar resultados por pagina de a 4, parametro para el http get. solo indicar la pagina
    #http://127.0.0.1:8000/list_all/?page=2 <<<<
    ordering = 'pk'
    model = Empleado #el modelo con el que trabajaremos
    #context_object_name = 'lista' #para acceder desde el template a la lista
"""

class listaempleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = '-pk'
    context_object_name = 'empleados'
    model = Empleado

########################################################################################


class porArea(ListView):
    template_name = 'persona/listarAreas.html'
    #queryset = Empleado.objects.filter(departamento__name='Area Contable')#error de Visual, funciona todo OK, filtrar con query
    #context_object_name = 'll'
    #en vez de retornarnos un modelo, nos retorna un query
    context_object_name = 'empleados'
    def get_queryset(self):
        area = self.kwargs['shorname'] #recojer el valor de la url
        lista = Empleado.objects.filter(departamento__shor_name=area) #forma practica de hacer lo mismo de arriba
        return lista

class porTrabajo(ListView):
    template_name = 'persona/list_trabajo.html'
    def get_queryset(self):
        trabajo = self.kwargs['work']
        query = Empleado.objects.filter(jobs=trabajo)
        return query

class empleadosbyKword(ListView):
    template_name = 'persona/empleadosbyKword.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword',)
        print('***********************')
        query = Empleado.objects.filter(first_name=palabra_clave)
        return query

class listaHabilidadesEmpleado(ListView):
    template_name = 'persona/listaHabilidadesEmpleado.html'
    context_object_name = 'habilidades'
    def get_queryset(self):
        empleado = Empleado.objects.get(id=3) #me recuperas un unico registro de la base de datos
        return empleado.habilidades.all()

##############################################################################################################################


class empleadoDetailView(DetailView): #detail view se usa para tomar el registro de una base de datos en especifico y ver todo sus datos
    model = Empleado
    template_name = "persona/detail_empleado.html" #en html lo veo con el {{object}} o el model en miniscula {{empleado}}

    def get_context_data(self, **kwargs):
        context = super(empleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context




################################################################################################################################


class EmpleadoCreateView(CreateView): #create view para ingresar registros a la BD
    model = Empleado
    template_name = "persona/add.html"
    #fields = ['first_name','last_name','jobs','departamento','habilidades','image'] #'Form' palabra clave para acceder desde el template
    form_class = EmpleadoForm
    #fields = ('__all__') # para ver todos los campos
    #success_url = '/succes' #para que se reidireccione a la misma pagina, mala practiva hacerlo asi
    success_url = reverse_lazy('persona_app:empleado-admin')

    def form_valid(self,form): #valida que los datos enviados sean correctos, los valida con el model
        empleado = form.save(commit=False) #alamcene todo en la base de datos desde el form, hace 1 vez el guardado
        empleado.full_name = empleado.first_name + '  ' + empleado.last_name
        empleado.save() #guarda cambios para impactarlo en la bD
        return super(EmpleadoCreateView, self).form_valid(form)

################################################################################################################################


class successView(TemplateView):
    template_name = "persona/succes.html"

##############################################################################################################################


class empleadoUpdate(UpdateView): #para acceder le mandamos el {{form}}
    template_name = "persona/update.html"
    fields = ['first_name','last_name','jobs','departamento','habilidades',]
    success_url = reverse_lazy('persona_app:empleado-admin')
    model = Empleado


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self,form):
        print('****x')
        return super(empleadoUpdate, self).form_valid(form)

##############################################################################################################################


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleado-admin')

##############################################################################################################################

