from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.core.mail import send_mail
from django.shortcuts import render, redirect



def contact(request):
    message_sent = False  # Flaga do wyświetlenia komunikatu

    if request.method == 'POST':
        # Otrzymaj dane z formularza
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Tutaj można dodać kod wysyłania e-maila, jeśli chcesz
        # Na razie pomijamy wysyłanie

        message_sent = True  # Zmieniamy flagę, aby wyświetlić komunikat

    return render(request, 'portfolio/contact.html', {'message_sent': message_sent})


def contact_success(request):
    return render(request, 'portfolio/contact_success.html')
