from django.db import models

# Create your models here.
from apps.integrantes.models import Integrante
ESCUELA_OPCION = (
    ('ecbti', 'ECBTI'),
    ('otra', 'OTRA'),
    ('otra1', 'OTRA1'),
)

TIPO_LINEA = (
    ('semillero', 'Semillero'),
    ('grado', 'Grado'),
)


class Semillero(models.Model):
    codigo = models.CharField(max_length=45)
    nombre = models.CharField (max_length=45)
    programa = models.CharField( max_length=45)
    fecha_creacion = models.DateField(null=True, blank=True, auto_now=True)
    lider = models.ForeignKey(
        Integrante,
        related_name='Semillero',
        on_delete=models.CASCADE
    )
    integrantes = models.ManyToManyField(Integrante, blank=True)
    
class Linea(models.Model):
    codigo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    escuela = models.CharField(max_length=45, choices=ESCUELA_OPCION)
    tipo = models.CharField(max_length=45, choices=TIPO_LINEA)
    fecha_creacion = models.DateField(null=True, blank=True, auto_now=True)