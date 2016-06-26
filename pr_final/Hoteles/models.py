

from django.db import models

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


class Comentario(models.Model) :
    contenido = models.TextField(default = "")
    hotel = models.ForeignKey(Hotel)
    idHotel = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now=True)

class HotelSelect (models.Model):
    idHotel = models.IntegerField(default="")
    usuario = models.CharField(max_length=32)
    fecha = models.DateTimeField(auto_now=True)

class Imagen(models.Model) :
    url_I = models.URLField(default="")
    img = models.ForeignKey(Hotel,default="")
    idHotel = models.IntegerField(default=0)

class StyleCSS (models.Model) :
    usuario = models.CharField(max_length=32)
    color = models.CharField(max_length=300,default="")
    size=models.CharField(max_length=200,default="")
    titulo_pagina = models.CharField(max_length = 32,default = "")
