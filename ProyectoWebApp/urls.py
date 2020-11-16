from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static 

# Importacion de la vistas
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.inicio, name='Inicio'),
    # path('servicios/', views.servicios, name='Servicios'),
    path('tienda/',views.tienda, name='Tienda'),
    # path('blog/', views.blog, name='Blog'),
    # path('contacto/', views.contacto, name='Contacto'),
    path('registrar/', views.cita, name='Cita'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # De esta manera podemos mostrar las imagenes