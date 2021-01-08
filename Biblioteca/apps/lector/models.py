from django.db import models
from apps.autor.models import Autor

# Create your models here.
from apps.libro.models import Libro

class Lector(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombres

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamos = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    def __str__(self):
        return self.libro.titulo
