#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from models import Hotel , HotelSelect , StyleCSS , Comentario , Imagen
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from xml_parser import myContentHandler
#from xml_parser import get
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
    if request.user.is_authenticated():
        log += 'Hola ' + request.user.username
        log += '<br><a href="/logout">Salir</a>'
    else:
        log += login()


    cuerpo += u'<span>Interfaz pública: para todos los usuarios</span>'
    cuerpo += '<br><ul style="list-style-type: square">'
    cuerpo += u'<li>Página principal: muestra los 10 alojamientos con más Comentarios y  un listado con las paginas personales.</li>'
    cuerpo += u'<li>Pagina personal de usuario: muestra los alojamientos seleccionadas por el usuario.</li>'
    cuerpo += '<li>Alojamientos: muestra todas los alojamientos disponibles. Permite filtrarlas por dos campos.</li>'
    cuerpo += u'<li>Cada alojamiento tiene su página con información más detallada.</li></ul>'
    cuerpo += u'<li>Además cada alojamiento tiene un enlace a su página correspondiente del Ayuntamiento de Madrid </li></ul>'
    cuerpo += '<span>Interfaz privada: solo para usuarios registrados </span>'
    #cuerpo += u'<li>g</li>
    cuerpo += u'Permite todas las funcionalidades de Interfaz pública y :'
    cuerpo += '<ul style="list-style-type: square">'
    cuerpo += u'<li>Seleccionar actividades en la pagina "todas" para su página personal.</li>'
    cuerpo += u'<li>Permite modificar varios aspectos de la página web, como el estilo o el título de su página personal.</li></ul>'

    #Logearse en ayuda

    #plantilla = get_template('template.html')
    c = Context({'loggin': log, 'contenido': cuerpo, 'titulo': titulo, 'inicio': inicio})
    #renderizado = plantilla.render(c)
    #return HttpResponse(renderizado)
    return render_to_response('template.html', c , context_instance = RequestContext(request))



def todos(request):
    lista = Hotel.objects.all()
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
    #usuarioStyle = User.objects.get(user = request.User.nombre)
    #context = {'lista' : lista , 'color': usuarioStyle.color , 'size':usuarioStyle.size , 'estrellas':filtro_estrellas , 'Subcategoria' : filtro_subcategoria}
    #return render_to_response('aloj.html',context,context_instance = RequestContext(request))
    c = Context ({'lista' : lista , 'estrellas':filtro_estrellas , 'subcategoria':filtro_subcategoria})
    return render_to_response('todos_alojamientos.html', c , context_instance = RequestContext(request))



def principal(request):

    respuesta=""
    salida=""
    lista=Hotel.objects.all()
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


    template = get_template("index.html")
    context = {'lista':lista[0:10],'user':request.user.username,'listausers':listauser,'condicion':""}
    if request.user.is_authenticated():
            try:
                us=User.objects.get(username=request.user.username)
            except User.DoesNotExist:
                context = {'lista':lista[0:10],'user':request.user.username}
                return render_to_response('index.html', context, context_instance = RequestContext(request))

            context = {'lista':lista[0:10],'user':request.user.username,'listausers':listauser,'condicion':""}
    return render_to_response('index.html', context, context_instance = RequestContext(request))


def new_user (request):
    log = '<form action = "" method ="POST">'
    log += 'Nombre de usuario<br><input type = "text" name = "Usuario"><br>'
    log += 'Password<br><input type="password" name="Password">'
    log += '<br><input type="submit" value="Registrarme">'
    log += '</form>'
    principal = '<a href="/">Princial</a>'
    if request.method == 'POST':
        username = request.POST['Usuario']
        password = request.POST['Password']
        lista = User.objects.all()
        for fila in lista :
            if fila.username == user :
                error = ""
                error += '<span>Error.</span><br>'
                error += 'El nombre de usuario está en uso . Introduzca otro'
                plantilla = get_template('index.html')
                c = Context({'loggin': log, 'inicio': inicio, 'error': error})
                renderizado = plantilla.render(c)
                return HttpResponse(renderizado)

        user = User.objects.create_user(username,username + '@ejemplo.com',password)
        user.save()
        user = User(nombre = username )
        user.save()
        #estilo_pagina = EstiloCss(usuario=usuario, banner='imagenes/alcala.png', login="", menu="red", pie="red")
        #estilo_pagina.save()
        return HttpResponseRedirect('/')

    #plantilla = get_template('template2.html')
    c = Context({'loggin': log})
    #renderizado = plantilla.render(c)
    #return HttpResponse(renderizado)
    return render_to_response('index.html', c, context_instance = RequestContext(request))

def alojamientoid (request , id):
    #poner los idiomas
    lista = Hotel.objects.get(id=id)
    imagelist = Imagen.objects.filter(idHotel = lista.id)
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
    usuario = Usuarios.objects.get(nombre=recurso)
    titulo = usuario.titulo_pagina
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
        pagina_estilo = StyleCSS.objects.get(usuario=recurso)
        log += 'Hola' + request.user.username
        log += '<br><a href = "/logaout">Salir</a>'

    if recurso == request.user.username :
        cambio_titulo += '<form action ="" method= "POST">'
        cambio_titulo += '<strong>Cambiar título de la pagina </strong><br><input type = "text" name = "Titulo">
        cambio_titulo += '<input type = "submit" value = "Cambiar" > '
        cambio_titulo += '</form>

        cambio_estilo += '<strong>Cambiar el estilo de la pagina </strong>'
        cambio_estilo +='<form action = "" method = "POST" </form>'
        cambio_estilo +='<label> Banner </label>
        cambio_estilo +='<select name = "banner"><option value = "" selected = selected > selecciona </option>'
        #tipos de Banner


#@csrf_exempt
def paginaUsuario(request , usuario) :
    print usuario
    listaHotel = []
    try:
        #css = StyleCSS.objects.get(usuario=usuario)
        #titulo = StyleCSS.titulo_pagina
        titulo = ""
        u = usuario
    except StyleCSS.DoesNotExist :
        usuario = Usuarios.objects.get(usuario = usuario)
        u = usuario.usuario
        titulo = ""
    try:
        hotelusu = Usuario.objects.get(hoteles)
        for hotel in hotelusu:
            imagenes = Imagen.objects.filter(alojamiento_id = alojamiento.alojamiento_id)
            if len(imagenes)>0:
                list_aloj.append((alojamiento, imagenes[0].url))
            else:
                list_aloj.append((alojamiento, ""))
    except ObjectDoesNotExist:
            print "No existen favoritos...
    template = get_template('user.html')
    context = RequestContext(request, {'alojamientos': listaHotel, 'usuario': u, 'titulo': titulo}) #le pasamos el objeto completo
    return HttpResponse(template.render(context))"""
