from django import forms

class MascotasFormulario(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    raza = forms.CharField(max_length=40)
    descripcion = forms.CharField(required=False)
    fechaNacimiento = forms.DateField(label='Fecha de Nacimiento')

class InformeFormulario(forms.Form):
    pass
class VeterinarioFormulario(forms.Form):
    pass
class ClienteFormulario(forms.Form):
    pass
