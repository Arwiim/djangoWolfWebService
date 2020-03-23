from django.contrib import admin
from django.urls import path
from . import views # el . hace referencia a estar donde estamos parados(la misma carpeta)


urlpatterns = [
    path('prueba/', views.pruebaView.as_view()), #Ias_view(submetodo)i ndica que trabajamos con vista generica
    path('vista/', views.pruebalistView.as_view()),
    path('vista2/', views.listaprueba.as_view()),
    path('registrer/', views.insertaregistro.as_view(), name='prueba_add'),
    path('fram/',views.frem.as_view()),
    path('resume/',views.ResumeFoundation.as_view(),name='resume_foundation'),
]