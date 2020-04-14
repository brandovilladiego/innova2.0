"""innovapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.paginas.views import inicio, nosotros, galeria, proyectos, eventos, contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('galeria/', galeria, name='galeria'),
    path('proyectos/', proyectos, name='proyectos'),
    path('eventos/', eventos, name='eventos'),
    path('contacto/', contacto, name='contacto'),
]
