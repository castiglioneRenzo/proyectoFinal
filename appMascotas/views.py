from django.shortcuts import render, HttpResponse
from appMascotas.models import *
from appMascotas.forms import *
# Create your views here.
def inicio(request):
    return render(request, 'landingPage.html')

def mascotaFormulario(request):
    titulo="AppMascotas - Nueva Mascota"
    titulo2="Nueva Mascota"
    if request.method == 'POST':
        miFormulario = MascotasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            mascota = Mascota(id=info['id'],nombre=info['nombre'],apellido=info['apellido'],raza=info['raza'],descripcion=info['descripcion'],fecha_nacimiento=info['fechaNacimiento'])
            mascota.save()
            return render(request, 'forms.html', {"titulo":titulo, "titulo2":titulo2})
    else:
        miFormulario = MascotasFormulario()
    return render(request, 'forms.html', {"miFormulario":miFormulario, "titulo":titulo, "titulo2":titulo2})