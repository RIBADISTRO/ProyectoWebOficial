from django.urls import path
from . import views
# Importacion de la vistas
urlpatterns = [    
    path('',views.tienda, name='Tienda'),
]