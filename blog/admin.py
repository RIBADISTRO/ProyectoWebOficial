from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):         # creamos la clase de solo
    readonly_fields=('created','updated')       # campos de lectura

class PostAdmin(admin.ModelAdmin):               # creamos la clase de solo
    readonly_fields=('created','updated')        # campos de lectura

admin.site.register(Categoria, CategoriaAdmin)   # registramos la clases de nuetro servicio
admin.site.register(Post, PostAdmin)             # registramos la clases de nuetro servicio