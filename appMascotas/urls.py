from django.urls import path
from appMascotas.views import *
urlpatterns = [
    path('', inicio, name='inicio'),
    path('mascota', mascotaFormulario, name='Mascota'),
]