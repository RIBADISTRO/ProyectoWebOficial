from django.shortcuts import render, HttpResponse
# from servicios.models import Servicio

# Create your views here.
def inicio(request):
    # return HttpResponse("Inicio")
    return render(request,'ProyectoWebApp/index.html')

""" def servicios(request):
    serviciosAll = Servicio.objects.all() # de esta forma le decimos a django que carge la class de nuestro  views
    # return HttpResponse("Servicio")
    return render(request,'ProyectoWebApp/servicios.html', {"serviciosAll" : serviciosAll}) """

def tienda(request):
    # return HttpResponse("Tienda")
    return render(request,'ProyectoWebApp/tienda.html')

""" def blog(request):
    # return HttpResponse("Blog")
    return render(request,'ProyectoWebApp/blog.html') """

""" def contacto(request):
    # return HttpResponse("Contacto")
    return render(request,'ProyectoWebApp/contacto.html') """

def cita(request):
    # return HttpResponse("Contacto")
    return render(request,'ProyectoWebApp/cita.html')