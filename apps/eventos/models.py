from django.db import models

# Create your models here.
from apps.integrantes.models import Integrante

TIPO_ACTIVIDAD = (
    ('taller', 'Taller'),
    ('capac', 'Capac'),
    ('wordshop', 'WordShop'),

)


class Evento(models.Model):
    codigo = models.CharField(
        max_length=45
    )
    nombre = models.CharField(max_length=45)
    lugar = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45, choices=TIPO_ACTIVIDAD)
    fecha_creacion = models.DateField()
    lider = models.ForeignKey(Integrante, on_delete=models.CASCADE, null=True, blank=True)
    fotos = models.FileField(upload_to="Fotografias", blank=True, null=True)

    def __str__(self):
        return self.nombre


