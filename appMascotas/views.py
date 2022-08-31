from django.shortcuts import render, HttpResponse
from appMascotas.models import *
from appMascotas.forms import *
# Create your views here.
def inicio(request):
    return render(request, 'landingPage.html')

# formulario de Mascotas
def mascotaFormulario(request):
    titulo="AppMascotas - Nueva Mascota"
    titulo2="Nueva Mascota"
    if request.method == 'POST':
        miFormulario = MascotasFormulario(request.POST)        
        if (miFormulario.is_valid()):
            info = miFormulario.cleaned_data
            mascota = Mascota(id=info['id'],nombre=info['nombre'],apellido=info['apellido'],raza=info['raza'],descripcion=info['descripcion'],fecha_nacimiento=info['fechaNacimiento'])
            mascota.save()
            return render(request, 'landingPage.html')
    else:
        miFormulario = MascotasFormulario()
    return render(request, 'forms.html', {"miFormulario":miFormulario, "titulo":titulo, "titulo2":titulo2})

#formulario de Informes
def informeFormulario(request):
    titulo="AppMascotas - Nuevo Informe"
    titulo2="Nuevo Informe"
    if request.method == 'POST':
        miFormulario = InformeFormulario(request.POST)
        if (miFormulario.is_valid()):
            info = miFormulario.cleaned_data
            informe = Informe(id_mascota=info['id_mascota'],fecha=info['fecha'],reporte=info['reporte'])
            informe.save()
            return render(request, 'landingPage.html')
    else:
        miFormulario = InformeFormulario()
    return render(request, 'forms.html', {"miFormulario":miFormulario, "titulo":titulo, "titulo2":titulo2})

#formulario de Veterinario
def veterinarioFormulario(request):
    titulo="AppMascotas - Nuevo Veterinario"
    titulo2="Nuevo Veterinario"
    if request.method == 'POST':
        miFormulario = VeterinarioFormulario(request.POST)
        if (miFormulario.is_valid()):
            info = miFormulario.cleaned_data
            vet = Veterinario(id=info['id'],nombre=info['nombre'],apellido=info['apellido'],dni=info['dni'],telefono=info['telefono'])
            vet.save()
            return render(request, 'landingPage.html')
    else:
        miFormulario = VeterinarioFormulario()
    return render(request, 'forms.html', {"miFormulario":miFormulario, "titulo":titulo, "titulo2":titulo2})

#formulario de Cliente
def clienteFormulario(request):
    titulo="AppMascotas - Nuevo Cliente"
    titulo2="Nuevo Cliente"
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        if (miFormulario.is_valid()):
            info = miFormulario.cleaned_data
            cliente = Cliente(id=info['id'],nombre=info['nombre'],apellido=info['apellido'],dni=info['dni'],telefono=info['telefono'])
            cliente.save()
            return render(request, 'landingPage.html')
    else:
        miFormulario = ClienteFormulario()
    return render(request, 'forms.html', {"miFormulario":miFormulario, "titulo":titulo, "titulo2":titulo2})

#Buscar informes por fecha
def buscarInformes(request):
    if  request.GET["Fecha"]:

        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
        fecha = request.GET['Fecha'] 
        informes = Informe.objects.filter(fecha__icontains=fecha)
        if len(informes) != 0:
            return render(request, "buscarInformes.html", {"informes":informes, "fecha":fecha})
        else:
            return render(request, 'buscarInformes.html', {"error":"No hay informes para esa fecha"})

    else: 
        return render(request, 'buscarInformes.html', {"error":"No se ingresaron datos"})
        # return HttpResponse("Ingresar Datos")
def buscar(request):
    return render(request, 'buscarInformes.html')