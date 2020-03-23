from django.db import models
#Siempre importante instalar las apps en settings para hacer correcto el migration
# Create your models here.
class Departamento(models.Model): #departamento va a ser una clase, un modelo de orm de django
    name = models.CharField('Nombre',max_length=50, blank=True, null=True) #el primer parametro hace referencia a como aparecera en el admin de django
                                                                #el blank refiere a que se pueden mandar datos en blanco, pero no son nullos, el null si quiere decir que puedo mandar nullo
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True) #por defecto todos los campos tienen que tener datos
                                                                    #unique para que sea unico el nombre corto
    anulate = models.BooleanField('Anulado',default=False, editable=False,blank=True,null=True) #mb + tab para el booleano, por defecto se creara falso a no ser que le especifiquemos
                                                                #no puede ser editable
                                
    class Meta:
        verbose_name = 'Departamentos' #verbose name para cambiar la visualizacion de nombre de la tabla
        verbose_name_plural = 'Areas Departamentos'
        ordering = ['pk','name'] #ordenar por id, por nombre, inversamente con el -
        unique_together = ('name','shor_name') #las combinaciones de name y shor name para que no se repitan al momento de registrar


    #def __str__(self):
    #    return str(self.pk) + ' - ' + self.name + ' - ' + self.shor_name #metodo para verlo en el admin # django crear id unicos internamente

    def __str__(self):
        return self.name + ' - ' + self.shor_name
