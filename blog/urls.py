from django.urls import path
from . import views
# from servicios import views
# from django.conf import settings
# from django.conf.urls.static import static 

# Importacion de la vistas
urlpatterns = [
    path('', views.blog, name='Blog'),
]
