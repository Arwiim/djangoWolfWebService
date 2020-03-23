from django import forms

class newDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    departamento = forms.CharField(max_length=50, required=True)
    nombre_corto = forms.CharField(max_length=50, required=True)
