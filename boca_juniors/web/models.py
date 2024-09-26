from django.db import models

from django.db import models

class Novedades(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.titulo

class Futbol(models.Model):
    jugador = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    goles = models.IntegerField()

    def __str__(self):
        return self.jugador

class Indumentaria(models.Model):
    producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.producto

