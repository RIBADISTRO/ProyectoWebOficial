from django.contrib import admin
from .models import Servicio # Importamos el app de nuestro servisios
# Register your models here.

class servicioAdmin(admin.ModelAdmin):      # creamos la clase de solo 
    readonly_fields=('created','updated')       # campos de lectura
    
admin.site.register(Servicio, servicioAdmin) # registramos la clases de nuetro servicio
