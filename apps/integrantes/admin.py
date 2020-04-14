from django.contrib import admin

# Register your models here.
from apps.integrantes.models import Integrante


@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    model = Integrante
    list_display = (
        'id', 'first_name', 'last_name', 'sexo', 'fecha_nacimiento',
        'programa', 'ciudad', 'centro'
    )
    list_editable = ('first_name', 'last_name')
    list_filter = ('sexo', 'programa', 'ciudad', 'centro')

