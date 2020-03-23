from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField #app de tercero

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidades'
        verbose_name_plural = 'Habilidades de Empleados'

    def __str__(self):
        return self.habilidad

# Create your models here.
class Empleado(models.Model):

    job_choices = (
        ('0','Administrador'),
        ('1','Contabilidad'),
        ('2','Economista'),
        ('3','Otro'),
    )

    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre Completo', max_length=80,blank=True,null=True)
    jobs = models.CharField('Trabajo',max_length=1,choices=job_choices,blank=True,null=True) # choices para seleccionar algun trabajo de la lista de arriba
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,blank=True,null=True) #primero parametro hace referencia a que tabla se va a relacionar.
    image = models.ImageField('Imagen',upload_to='empleado',blank=True, null=True) #mim + tab para campo de imagenes
    habilidades = models.ManyToManyField(Habilidades) #m2m + tab relacion muchos a muchos
    hoja_vida = RichTextField(blank=True,null=True)
    class Meta:
        verbose_name = 'Personas Empleados'
        verbose_name_plural = 'Empleados'
        #ordering = ['first_name','last_name']
        ordering = ['-pk']
        unique_together = ('first_name','last_name')
    
    def __str__(self):
        return str(self.pk) + ' - ' + self.first_name + ' - '+ self.last_name


    
