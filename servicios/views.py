from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicios(request):
    serviciosAll = Servicio.objects.all()  # de esta forma le decimos a django que carge la class de nuestro  views
    return render(request,'servicios/servicios.html', {"serviciosAll":serviciosAll})