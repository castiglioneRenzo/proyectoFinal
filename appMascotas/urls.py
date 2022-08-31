from django.urls import path
from appMascotas.views import *
urlpatterns = [
    path('', inicio, name='inicio'),
    path('mascota', mascotaFormulario, name='Mascota'),
    path('cliente', clienteFormulario, name='Cliente'),
    path('veterinario', veterinarioFormulario, name='Veterinario'),
    path('informe', informeFormulario, name='Informe'),
    path('buscarInformes/', buscarInformes, name='buscarInformes'),
    path('buscar',buscar, name='qInformes'),
]