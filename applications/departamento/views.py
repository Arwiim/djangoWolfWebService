from django.shortcuts import render
#Todas las vistas genericas necesitaran un template para trabjar
# Create your views here.
from .forms import newDepartamentoForm
from django.views.generic.edit import FormView #vista generica para trabajar con varios modelos
from django.views.generic import ListView
from applications.persona.models import Empleado
from .models import Departamento
from django.urls import reverse_lazy


class departamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'

####################################################################################

class newDepartamento(FormView):
    template_name = 'departamento/new_dpt.html'
    form_class = newDepartamentoForm
    success_url = reverse_lazy('departamento_app:departamento_list')

    def form_valid(self, form):
        print('********************')

        depa = Departamento(name=form.cleaned_data['departamento'],
                            shor_name=form.cleaned_data['nombre_corto'])
        
        depa.save()#para guardarlo en la bd, instancia de clase

        print('ASDASDNASLKDNASLKDNASKNDKASNDLAKSNALSKNDLSAKNDLAKSNDLASK')

        nombre = form.cleaned_data['nombre'] #recuperar datos del formulario
        apellido = form.cleaned_data['apellido']

        Empleado.objects.create(first_name=nombre,
                                last_name=apellido,
                                jobs='1',
                                departamento=depa)

        return super(newDepartamento, self).form_valid(form)
