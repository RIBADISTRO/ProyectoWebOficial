from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    # return HttpResponse("Inicio")
    return render(request,'ProyectoWebApp/index.html')

def servicios(request):
    # return HttpResponse("Servicio")
    return render(request,'ProyectoWebApp/servicios.html')

def tienda(request):
    # return HttpResponse("Tienda")
    return render(request,'ProyectoWebApp/tienda.html')

def blog(request):
    # return HttpResponse("Blog")
    return render(request,'ProyectoWebApp/blog.html')

def contacto(request):
    # return HttpResponse("Contacto")
    return render(request,'ProyectoWebApp/contacto.html')

def cita(request):
    # return HttpResponse("Contacto")
    return render(request,'ProyectoWebApp/cita.html')