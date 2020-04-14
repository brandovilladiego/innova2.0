from django.contrib import admin

# Register your models here.
from apps.eventos.models import Evento

admin.site.register(Evento)
