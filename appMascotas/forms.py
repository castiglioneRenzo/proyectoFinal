from django import forms

class MascotasFormulario(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    raza = forms.CharField(max_length=40)
    descripcion = forms.CharField(required=False)
    fechaNacimiento = forms.DateField(label='Fecha de Nacimiento')

class InformeFormulario(forms.Form):
    fecha = forms.DateField()
    id_mascota = forms.IntegerField(label="ID de Mascota")
    reporte = forms.CharField()

class VeterinarioFormulario(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()

class ClienteFormulario(forms.Form):
    id = forms.IntegerField()
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    dni=forms.IntegerField()
    telefono=forms.IntegerField()
