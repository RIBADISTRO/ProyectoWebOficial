"""ProyectoWebOficial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
# from ProyectoWebApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')),  #Registro la app servicio
    path('blog/', include('blog.urls')),            #Regitro la app blog
    path('contacto/', include('contacto.urls')),    #Registro la app contacto
    path('tienda/', include('tienda.urls')),        #Registro la app tienda
    path('', include('ProyectoWebApp.urls')),       #Registro la app ProyectoWebApp
    
]

