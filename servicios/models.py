from django.db import models
"""
    Modelos <https://docs.djangoproject.com/en/3.1/topics/db/models/>
    Un modelo es la fuente única y definitiva de información sobre sus datos.
    Contiene los campos y comportamientos esenciales de los datos que está
    almacenando. Generalmente, cada modelo se asigna a una sola tabla de
    base de datos. 

    $ python manage.py migrate ""
    $ python manage.py makemigrations 

    """

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios') # dentro de los parendecis poner el nombre de la apalicacion
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    # Un método __str__() le dice a Python como mostrar la representación "string" de un objeto
    def __str__(self):
        return self.titulo

        
""" https://tutorial.djangogirls.org/es/django_admin/ """