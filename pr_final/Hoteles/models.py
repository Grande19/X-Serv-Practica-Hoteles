from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel (models.Model):
    nombre = models.CharField(max_length = 32)
    url = models.URLField()
    direccion = models.TextField(max_length = 200)
    #fecha_seleccion = models.DateField(blank=True)
    descripcion = models.TextField(default="")
    estrellas = models.CharField(max_length = 32)
    tipo = models.CharField(max_length = 32,default="")
    urlimagen = models.URLField()

class SelectedHotel (models.Model):
    idHotel = models.ForeignKey(Hotel)
    usuario = models.ForeignKey(User,default = "")
    fecha_seleccion = models.DateField(null = True , blank = True)



class Comentario(models.Model) :
    contenido = models.TextField(default = "")
    hotel = models.ForeignKey(Hotel)
    idHotel = models.IntegerField(default=0)
    date = models.DateField ( null=True , blank= True)
    usuario = models.ForeignKey(User)


class Imagen(models.Model) :
    url_I = models.URLField(default="")
    img = models.ForeignKey(Hotel,default="")
    idHotel = models.IntegerField(default=0)

class CSS (models.Model) :
    usuario = models.ForeignKey(User)
    color = models.CharField(max_length=300,default="")
    size=models.CharField(max_length=200,default="")
    titulo = models.CharField(max_length = 32,default = "")
