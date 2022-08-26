from django.db import models
class Mascota(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    descripcion = models.TextField()
    fecha_nacimiento = models.DateField()
def __str__(self):
    return self.nombre + " " + self.apellido

class Informe(models.Model):
    fecha = models.DateField()
    id_mascota = models.IntegerField(null=False)
    reporte = models.TextField()
    def __str__(self):
        return str(self.fecha) + " " + self.id_mascota

class Veterinario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    telefono=models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.apellido

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    telefono=models.IntegerField()
    
    def __str__(self):
        return self.nombre + " " + self.apellido