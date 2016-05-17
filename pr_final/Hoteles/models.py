from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hotel (models.Model):
    nombre = models.CharField(max_length = 32)
    estrellas = models.IntegerField()
    url = models.URLField()
    direccion = models.TextField(max_length = 200)

class User (models.Model) :
    nombre = models.CharField(max_length = 32)
    titulo_pagina = models.CharField(max_length = 32)
    hoteles = models.ManyToManyField(Hotel)

class Comentario(models.Model) :
    contenido = models.TextField()
    hotel = models.ManyToManyField(Hotel)



class StyleCSS (models.Model) :
    usuario = models.TextField(blank=True)
    banner = models.TextField(blank=True)
    login = models.TextField(blank=True)
    menu = models.TextField(blank=True)
    pie = models.TextField(blank=True)
