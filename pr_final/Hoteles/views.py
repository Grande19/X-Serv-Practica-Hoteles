#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render




from models import Hotel , HotelSelect , StyleCSS , Comentario , Imagen

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from xml_parser import myContentHandler
#from django.core.context_procesors import csrf
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist
import urllib , urllib2
#from xml_parser import CounterHandler
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    return render_to_response('login.html',RequestContext(request,{}))

def auth_view(request):


    listauser = User.objects.all()
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    #c = Context({'nombre':request.user.username})
    #return render_to_response('index.html', RequestContext(request),c)
    user = auth.authenticate(username = username , password = password)

    if user is not None :
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin (request):
    return render_to_response('loggedin.html',{'full_name':request.user.username})

def invalid_login (request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')






# Create your views here.


def loggear(request):
    if request.method == "POST" :
        user

def about(request):
    cuerpo = ""
    log = ""
    titulo = "About this page"
    inicio = '<a href = "/">Principal</a>'


    cuerpo = ""
    log = ""
    titulo = u"About. Información Alojamientos de Madrid"
    inicio = '<a href="/">Inicio</a>'
    error = ''


    #Logearse en ayuda

    #plantilla = get_template('template.html')
    c = Context({ 'contenido': cuerpo, 'titulo': titulo, 'inicio': inicio})
    #renderizado = plantilla.render(c)
    #return HttpResponse(renderizado)
    return render_to_response('about.html', c , context_instance = RequestContext(request))



def todos(request):
    lista = Hotel.objects.all()

    listausu = User.objects.all()

    #listausu = Usuarios.objects.all()

    filtro_estrellas = ""
    filtro_subcategoria = ""
    if request.method == 'POST':
        filtro_estrellas = request.POST.get('estrellas',"")
        print filtro_estrellas
        filtro_subcategoria = request.POST.get('ftipo',"")
        print filtro_subcategoria
        if filtro_estrellas != "" and filtro_subcategoria != "" :
            lista = Hotel.objects.filter(tipo = filtro_estrellas,estrellas = filtro_estrellas)
        elif filtro_estrellas == "" and filtro_subcategoria != "":
            lista=Hotel.objects.filter(tipo=filtro_subcategoria)
        elif filtro_subcategoria == "" and filtro_estrellas != "":
            lista=Hotel.objects.filter(estrellas=filtro_estrellas)
    #Usertyle = User.objects.get(user = request.User.nombre)
    #context = {'lista' : lista , 'color': Usertyle.color , 'size':Usertyle.size , 'estrellas':filtro_estrellas , 'Subcategoria' : filtro_subcategoria}
    #return render_to_response('aloj.html',context,context_instance = RequestContext(request))
    c = Context ({'lista' : lista , 'estrellas':filtro_estrellas , 'subcategoria':filtro_subcategoria})
    return render_to_response('todos_alojamientos.html', c , context_instance = RequestContext(request))



def principal(request):

    respuesta=""
    salida=""
    lista=Hotel.objects.all()

    listauser=User.objects.all()

    listauser=""

    #User es el admin el creo por defecto que no guardo en models
    print listauser

    if len(lista) == 0:
        print("Parsing....")
        theParser = make_parser()
        theHandler = myContentHandler()
        theParser.setContentHandler(theHandler)
        fil = urllib2.urlopen( 'http://www.esmadrid.com/opendata/alojamientos_v1_es.xml')
        theParser.parse(fil)

    #autenticado = request.user.is_authenticated()
    #if autenticado == True:
    #    user = User.objects.get(nombre=request.user.username)
    #else
    #    return render_to_response('invalid_login.html')
    template = get_template("index.html")
    context = {'lista':lista[0:10],'user':request.user.username,'listausers':listauser,'condicion':""}
    autenticado = request.user.is_authenticated
    if autenticado:
            try:
                usuario=User.objects.get(username=request.user.username)
            except User.DoesNotExist:
                context = {'lista':lista[0:10],'user':request.user.username}
                return render_to_response('index.html', context, context_instance = RequestContext(request))

    listausers = User.objects.all()
    context = {'autenticado': request.user.is_authenticated, 'lista':lista[0:10],'user':request.user.username,'listausers':listauser,'condicion':" "}
    return render_to_response('index.html', context, RequestContext(request))




def alojamientoid (request , id):
    #poner los idiomas
    lista = Hotel.objects.get(id=id)
    imagelist = Imagen.objects.filter(idHotel = lista.id)

    listausu = User.objects.all()
    autenticado = request.user.is_authenticated
    listacomment = Comentario.objects.filter(idHotel=lista.id)

    if request.method == 'POST' :
        value = request.POST.get("comentario","")
        print "haciendo post"
        if value!="":
            comentario = Comentario (idHotel = lista.id , contenido = value , hotel = lista)
            comentario.save()
            print comentario.contenido
        else :
            comentario = Comentario.objects.filter(idHotel = lista.id)
            print comentario
    listacomment =Comentario.objects.filter(idHotel=lista.id)
    context = {'autenticado':autenticado,'lista':imagelist[0:5],'h':lista,'condicion':"",'url':lista.url,'name':lista.nombre, 'body':lista.descripcion,
                'address':lista.direccion,'comentarios':listacomment,'type':lista.tipo,'stars':lista.estrellas}

    listausu = ""
    Comentario = ""

    if request.method == 'POST' :
        value = request.POST.get("Comentario","")
        if value!="":
            Comentario = Comentario (idHotel = lista.id , contenido = value , hotel = lista.nombre )
            Comentario.save()
            print Comentario.contenido
        else :
            Comentario = Comentario.objects.filter(idHotel = lista.id)
            print Comentario
    listaComentario =""
    context = {'lista':imagelist[0:5],'h':lista,'condicion':"",'url':lista.url,'name':lista.nombre, 'body':lista.descripcion,
                'address':lista.direccion,'Comentarios':listaComentario,'type':lista.tipo,'stars':lista.estrellas,

                'user':request.user.username,'listausers':listausu}
    #if request.user.is_authenticated():
    #    us=PagUser.objects.get(user=request.user.username)
    #    context = {'lista':listimages[0:5],'h':hoteles,'condicion':"",'url':lista.url,'name':lista.name,
    #                'address':lista.address,'Comentarios':listcoms,'type':lista.tipo,'stars':lista.stars, 'body':lista.body,
    #                'color':us.color,'size':us.size,'user':request.user.username,'listausers':listauser}

    return render_to_response('alojamiento_id.html', context,context_instance = RequestContext(request))
    #return HttpResponse(imagelist.idHotel)




"""
def pagina_usuario (request , recurso) :
    cuerpo = ""
    usuario = User.objects.get(username=recurso)
    #titulo = usuario.titulo_pagina
    log = ""
    error = ""
    cambio_titulo = ""
    cambio_estilo = ""
    #poner el menu en el template
    if titulo == "" :
        titulo = u'Pagina de' + usuario.nombre
    try:
        hoteldeusu = usuario.hotel.all()
        hoteldeusu = hoteldeusu.values ()
        aux = 0
        while (aux < len (hoteldeusu)):

            hotel = hoteldeusu[aux]['nombre']


    except ObjectDoesNotExist :
        return HttpResponse('NO')

    if request.user.is_authenticated ():
        #pagina_estilo = StyleCSS.objects.get(usuario=recurso)
        log += 'Hola' + request.user.username
        log += '<br><a href = "/logaout">Salir</a>'

    if recurso == request.user.username :
        cambio_titulo += '<form action ="" method= "POST">Cambiar título de la pagina<br><input type = "text" name = "Titulo"'

        cambio_titulo += '<input type = "submit" value = "Cambiar" > '
        cambio_titulo += '</form>'

        cambio_estilo += '<strong>Cambiar el estilo de la pagina </strong>'
        cambio_estilo +='<form action = "" method = "POST" </form><label> Banner </label>'

        cambio_estilo +='<select name = "banner"><option value = "" selected = selected > selecciona </option>'
        #tipos de Banner
    emplate = get_template('user.html')
    context = RequestContext(request, {'alojamientos': listaHotel, 'usuario': u, 'titulo': titulo}) #le pasamos el objeto completo
    return HttpResponse(template.render(context))"""


#@csrf_exempt
def paginaUsuario(request , usuario) :
    u = usuario
    print u
    listaHotel = []
    titulo = ""
    if u == "alojamientos":
        lista = Hotel.objects.all()
        listausu = User.objects.all()
        filtro_estrellas = ""
        filtro_subcategoria = ""
        if request.method == 'POST':
            filtro_estrellas = request.POST.get('estrellas',"")
            print filtro_estrellas
            filtro_subcategoria = request.POST.get('ftipo',"")
            print filtro_subcategoria
            if filtro_estrellas != "" and filtro_subcategoria != "" :
                lista = Hotel.objects.filter(tipo = filtro_estrellas,estrellas = filtro_estrellas)
            elif filtro_estrellas == "" and filtro_subcategoria != "":
                lista=Hotel.objects.filter(tipo=filtro_subcategoria)
            elif filtro_subcategoria == "" and filtro_estrellas != "":
                lista=Hotel.objects.filter(estrellas=filtro_estrellas)
        #Usertyle = User.objects.get(user = request.User.nombre)
        #context = {'lista' : lista , 'color': Usertyle.color , 'size':Usertyle.size , 'estrellas':filtro_estrellas , 'Subcategoria' : filtro_subcategoria}
        #return render_to_response('aloj.html',context,context_instance = RequestContext(request))
        c = Context ({'lista' : lista , 'estrellas':filtro_estrellas , 'subcategoria':filtro_subcategoria})
        return render_to_response('todos_alojamientos.html', c , context_instance = RequestContext(request))
    elif u == "about" :
        cuerpo = ""
        log = ""
        titulo = "About this page"
        inicio = '<a href = "/">Principal</a>'


        cuerpo = ""
        log = ""
        titulo = u"About. Información Alojamientos de Madrid"
        inicio = '<a href="/">Inicio</a>'
        error = ''

        #Logearse en ayuda

        #plantilla = get_template('template.html')
        c = Context({'contenido': cuerpo, 'titulo': titulo, 'inicio': inicio})
        #renderizado = plantilla.render(c)
        #return HttpResponse(renderizado)
        return render_to_response('about.html', c , context_instance = RequestContext(request))

    elif u == "accounts/logout":
        auth.logout(request)
        return render_to_response('logout.html')
    elif u == "accounts/login":
        autenticado = request.user.is_authenticated
        username = request.user.username
        context = {'autenticado':autenticado , 'user':username}

        return render_to_response('login.html',context,RequestContext(request,{}))
    elif u == "accounts/auth":
        listauser = User.objects.all()
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        #c = Context({'nombre':request.user.username})
        #return render_to_response('index.html', RequestContext(request),c)
        user = auth.authenticate(username = username , password = password)

        if user is not None :
            auth.login(request,user)
            return HttpResponseRedirect('/accounts/loggedin')
        else:
            return HttpResponseRedirect('/accounts/invalid')
    elif u == "accounts/loggedin":
        return render_to_response('loggedin.html',{'full_name':request.user.username})




    else:


        try:
            css = StyleCSS.objects.all()
            #titulo  = CSS.titulo
            titulo = ""
            u = usuario
        except StyleCSS.DoesNotExist :
            usuario = User.objects.get(usuario = usuario)
            u = usuario.usuario
            titulo = ""
        try:
            hotelusu = HotelSelect.objects.all()
            #for idHotel in hotelusu:
            #imagenes = Imagen.objects.filter(idHotel = alojamiento.alojamiento_id)
            #if len(imagenes)>0:
            #    list_aloj.append((alojamiento, imagenes[0].url))
            #else:
            #    list_aloj.append((alojamiento, ""))
        except HotelSelect.DoesNotExist:
            print "No existen favoritos..."

    #template = get_template('user.html')
    context = {'alojamientos': listaHotel, 'usuario': u, 'titulo': titulo} #le pasamos el objeto completo
    return render_to_response ('user.html',context,RequestContext(request))
