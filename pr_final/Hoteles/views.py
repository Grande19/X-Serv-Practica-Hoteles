#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from models import Hotel , User , StyleCSS , Comentario
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from xmlp_arser import get
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist
import urllib2

# Create your views here.

def login(): #registro de usuario

    user = '<form action="" method="POST">'
    user += 'Nombre de usuario<br><input type="text" name="Usuario"><br>'
    user += 'Password<br><input type="password" name="Password">'
    user += '<br><input type="submit" value="Entrar"> o '
    user += '<a href="/register">Registrate</a>'
    user += '</form>'
    return user

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def pie_pagina():
    pie = "Copyright . Esta aplicacion utiliza datos del portal de datos abierto de la ciudad de Madrid "
    pie += '<a href="http://bit.ly/1T24Zsq">Descripción de los datos</a>'
    pie += '<a href="http://www.esmadrid.com/opendata/alojamientos_v1_es.xml">Listado de hoteles en XML</a>'
    return pie
