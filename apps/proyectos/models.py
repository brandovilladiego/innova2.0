from django.db import models

# Create your models here.
from apps.integrantes.models import Integrante

TIPO_PROYECTO = (
    ('semillero', 'Semillero'),
    ('grado', 'Grado')
)


class Proyecto(models.Model):
    codigo = models.CharField(
        max_length=45,
        help_text='El código debe ser numérico'
    )
    nombre = models.CharField(max_length=45)
    lider = models.ForeignKey(
        Integrante,
        related_name='proyectos',
        on_delete=models.CASCADE
    )
    descripcion = models.CharField(max_length=300)
    integrantes = models.ManyToManyField(Integrante, blank=True)
    tipo = models.CharField(max_length=45, choices=TIPO_PROYECTO)
    fecha_creacion = models.DateField(null=True, blank=True, auto_now=True)
    foto = models.FileField(upload_to="foto_proyectos", blank=True, null=True)

    def __str__(self):
        return self.nombre

