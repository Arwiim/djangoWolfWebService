from django.contrib import admin
from django.urls import path



from . import views

app_name = "persona_app" #etiqueta para llamarla desde afuera, hace referencia a todo el conjunto

urlpatterns = [

    path('', views.InicioView.as_view(), name='inicio'), #url por defecto se defini '' en primer parametro

    path('list_all/', views.listallempleados.as_view(),name='empleados_all'),
    path('listarAreas/<shorname>/', views.porArea.as_view(),name="porArea"), #Importar vistas !!!!!!!"!!!!!"·$"!$·!"$"·%"·$% aca va la funcion de las vistas
    #shorname va como parametro para recojer ese valor


    path('listarTrabajo/<work>', views.porTrabajo.as_view()),
    path('listarEmpleadosKword/',views.empleadosbyKword.as_view()),
    path('listarHabilidades-empleado/',views.listaHabilidadesEmpleado.as_view()),
    path('verempleado/<pk>',views.empleadoDetailView.as_view(),name='empleado_detalle'), #si o si paramentro de pk
    path('add/',views.EmpleadoCreateView.as_view(),name='empleador_add'),
    path('succes/',views.successView.as_view(), name = 'correcto'), #vista generica para que se reideccione al añadir un usuario, segundo parametro para id de la url
    path('update/<int:pk>', views.empleadoUpdate.as_view(), name = 'modficar_empleado'),
    path('delete-empleado/<pk>',views.EmpleadoDeleteView.as_view(), name = 'eliminar_empleado'), #no usar mismo nombre de urls que para las vistas
    path('lista-empleados-admin',views.listaempleadosAdmin.as_view(),name='empleado-admin'), #url para administrar
]
