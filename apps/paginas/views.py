from django.core.mail import send_mail
from django.shortcuts import render

from innovapp.forms import ContactForm
from apps.integrantes.models import Integrante
from apps.proyectos.models import Proyecto
from apps.eventos.models import Evento
from django.core.mail import send_mail

def inicio(request):
    return render(request, 'inicio.html')


def nosotros(request):
    lista_integrantes = Integrante.objects.filter(is_active=True)
    return render(request, 'nosotros.html', locals())


def galeria(request):
    return render(request, 'galeria.html')


def proyectos(request):
    lista_proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', locals())


def eventos(request):
    lista_eventos = Evento.objects.all()
    return render(request, 'eventos.html', locals())


def contacto(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        message = form.cleaned_data.get("message")
        email = form.cleaned_data.get("email")

        subject = 'Contact form'
        from_email = 'postmaster@sandbox63ff52590f944940b74a86150b63c307.mailgun.org'
        to_email = [from_email, 'eduardopalacios38@gmail.com']
        contact_message = "%s: %s via %s" % (
            name,
            message,
            email)

        send_mail(subject,
                  message,
                  'postmaster@sandbox63ff52590f944940b74a86150b63c307.mailgun.org',
                  ['eduardopalacios38@gmail.com'],
                  fail_silently=False)

    return render(request, 'contacto.html')
