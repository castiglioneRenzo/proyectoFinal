from django.shortcuts import render, HttpResponse
from appMascotas.models import *
from appMascotas.forms import *
# Create your views here.
def inicio(request):
    return render(request, 'landingPage.html')

def mascotaFormulario(request):
    if request.method == 'POST':
        miFormulario = MascotasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            mascota = Mascota(id=info['id'],nombre=info['nombre'],apellido=info['apellido'],raza=info['raza'],descripcion=info['descripcion'],fecha_nacimiento=info['fechaNacimiento'])
            mascota.save()
            return render(request, 'landingPage.html')
    else:
        miFormulario = MascotasFormulario()
    return render(request, 'mascotaForm.html', {"miFormulario":miFormulario})