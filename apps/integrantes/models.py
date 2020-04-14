from django.contrib.auth.models import User
from django.db import models

# Create your models here.
SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
)

PROGRAMA = (
    ('ing_sistemas', 'Ingenieria de Sistemas'),
    ('ing_telecomunicaciones', 'Ingenieria de Telecomunicaciones'),
    ('ing_industrial', 'Ingenieria de Industrial'),
)

TIPO = (
    ('estudiante', 'Estudiante'),
    ('docente', 'Docente'),
    ('externo', 'Externo')
)


class Integrante(User):
    identificacion = models.CharField(max_length=45)
    sexo = models.CharField(max_length=1, choices=SEXO)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12, null=True, blank=True)
    direccion = models.CharField(max_length=45, null=True, blank=True)
    programa = models.CharField(max_length=45, choices=PROGRAMA)
    ciudad = models.CharField(max_length=45)
    centro = models.CharField(max_length=45)
    foto = models.FileField(upload_to='foto_integrante', null=True, blank=True )

    def __str__(self):
        return self.get_full_name()
