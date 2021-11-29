from django.db.models.query_utils import subclasses
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContactForm
from django.conf import settings
from django.core.mail import message, send_mail
from django.http import JsonResponse, request
import time
# Create your views here.

def ejecutaAJAX(request):
    if request.method == 'POST':
        print('+++')
        opcion = request.POST.get('valor', '')
        respuesta = {}
        respuesta['status'] = 'correcto'
        opciones = {}
        if opcion == '1':
            opciones['1'] = 'Santa Lucía del Camino'
            opciones['2'] = 'Santa Cruz Xoxocotlán'
            opciones['3'] = 'San Raymundo Jalpan'
            opciones['4'] = 'Oaxaca de Juárez'
            time.sleep(5);
        elif opcion == '2':
            opciones['1'] = 'Tehuacán'
            opciones['2'] = 'Amozoc'
            opciones['3'] = 'Puebla de Zaragosa'
            time.sleep(3)
        else: 
            respuesta['status'] = 'error de opción'
        respuesta['opciones'] = opciones
        return JsonResponse(respuesta)
            
            

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        print("hola..........................................")
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name","")
            email = request.POST.get("email","")
            content = request.POST.get("content","")
            # print(name)
            link = reverse('contact')
            # print(link)
            subject = "Gracias por contactarnos"
            message = "Hola {name}, gracias por tu mensaje"
            email_from = settings.EMAIL_HOST_USER
            email_for = [email,]
            send_mail(subject,message,email_from,email_for)
            return redirect(link+'?ok')
    return render(request,'contact/contact.html',{'form':contact_form})