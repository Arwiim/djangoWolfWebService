from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Empleado
        fields = ('first_name','last_name','jobs','departamento','image','habilidades')

        widgets = {
            'habilidades' : forms.CheckboxSelectMultiple()
        }
