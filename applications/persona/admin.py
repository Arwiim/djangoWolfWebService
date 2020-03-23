from django.contrib import admin
from .models import Empleado, Habilidades
#Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin): #clase internad e django
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'jobs',
        'full_name',
        'image',
        'id',
    )
    #Funcion para el full name
    def full_name(self, obj):
    #print(obj.first_name) #referencia al objeto de Empleado
        return obj.first_name + '  ' + obj.last_name
    #
    
    search_fields = ('first_name',)

    list_filter = ('jobs','habilidades','departamento',)

    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
