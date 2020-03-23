#personalizar el form del html
from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Prueba
        #fields = ('__all__') #all para mostrar todos los campos del modelo prueba
        fields = ('titulo','subtitulo','cantidad',)

        widgets = {'titulo': forms.TextInput(attrs= {'placeholder':'Ingrese Texto',
                                                     'class':'ola'})} #atrs sirve para personalziar form html, 

    def clean_cantidad(self): #validar numero de cantidad
        cantidad = self.cleaned_data['cantidad'] #funcion para recuperar el valor de cantidad
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero Mayor a 10')

        return cantidad    
