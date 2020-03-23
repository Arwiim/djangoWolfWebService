from django.db import models

# Create your models here.
# las tablas son clases
class Prueba(models.Model):
    titulo = models.CharField(max_length=30) #CHARFIELD = TEXTO
    subtitulo = models.CharField( max_length=50) #mcchar + tab crea directamente el CharField
    cantidad = models.IntegerField() #mint + tab crea IntegrerField

    def __str__(self): #metodo string para los objetos para poder mostrarlos
        return self.titulo +  '  ' + self.subtitulo #+ self.cantidad

    