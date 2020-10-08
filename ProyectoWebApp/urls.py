from django.urls import path
from ProyectoWebApp import views

# Importacion de la vistas
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.inicio, name='Inicio'),
    path('servicios/', views.servicios, name='Servicios'),
    path('tienda/',views.tienda, name='Tienda'),
    path('blog/', views.blog, name='Blog'),
    path('contacto/', views.contacto, name='Contacto'),
    path('registrar/', views.cita, name='Cita'),
]
