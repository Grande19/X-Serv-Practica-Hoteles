

# Create your views here.
#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from models import Hotel , HotelSelect , StyleCSS , Comentario , Image
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from xml_parser import myContentHandler
import xml.etree.ElementTree as ET
import datetime
from operator import itemgetter
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist
import urllib , urllib2
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



def about(request):


    return render_to_response('about.html', context_instance = RequestContext(request))



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
    orderlist = []

    print lista
    listauser=User.objects.all()
    #User es el admin el creo por defecto que no guardo en models
    print listauser

    if len(lista) == 0:
        print("Parsing....")
        theParser = make_parser()
        theHandler = myContentHandler()
        theParser.setContentHandler(theHandler)
        fil = urllib2.urlopen( 'http://www.esmadrid.com/opendata/alojamientos_v1_es.xml')
        theParser.parse(fil)

    orderlist = comentarios(lista)
    cont = 10
    for item in orderlist:
        if cont > 0 and item[1]>0:
            cont = cont -1
            try:
                hotel = Hotel.objects.get(id = item[0])
                imagen = Image.objects.filter(idHotel = hotel.id)
                usuarios = User.objects.all()
            except ObjectDoesNotExist:
                print "No existe el hotel"

    print orderlist
    template = get_template("index.html")
    context = {'lista':orderlist,'user':request.user.username,'listausers':listauser,'condicion':""}
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

def alojamiento_frances(request,id):
    disponible_idioma = False
    traduccion = urllib2.urlopen('http://www.esmadrid.com/opendata/alojamientos_v1_fr.xml')
    tree = ET.parse(traduccion)
    root = tree.getroot()
    hotel = Hotel.objects.get(id=id)
    print hotel.nombre
    for child in root.iter('BasicData'):
        nombre = child.find('name').text

        if nombre == hotel.nombre:
            disponible_idioma = True
            descripcion = child.find('body').text
            web = child.find('web').text
            if descripcion == None:
                descripcion = "Hotel description do not avaliable in english"
            if web == None :
                web = "Web do not avaliable in english "
            break ;
    if not disponible_idioma:
        return HttpResponse ("Hotel do not avaliable in english")
    for child in root.iter('geoData'):
        direccion = child.find('address').text
        if direccion == hotel.direccion:
            pais = child.find ('country').text
        break ;
    for child in root.iter('media'):
        url = child.find('url').text

        if url == hotel.url:

            break;




def alojamientoid (request , id):
    traduccioningles = request.path+"/english"
    traduccionfrances = request.path+"/francais"
    lista = Hotel.objects.get(id=id)
    imagelist = Image.objects.filter(idHotel = lista.id)

    listausu = User.objects.all()
    autenticado = request.user.is_authenticated


    if request.method == 'POST' :
        value = request.POST.get("comentario","")
        print "haciendo post"
        cn = lista.numbercom+1
        lista.numbercom = n
        lista.save
        comentario = Comentario (idHotel = lista.id , contenido = value , hotel = lista)
        comentario.save()
        print comentario.contenido

    listacomment =Comentario.objects.filter(idHotel=lista.id)
    context = {'autenticado':autenticado,'lista':imagelist[0:5],'h':lista,'condicion':"",'url':lista.url,'name':lista.nombre, 'body':lista.descripcion,'user':request.user.username,'listausers':listausu,
                'address':lista.direccion,'comentarios':listacomment,'type':lista.tipo,'stars':lista.estrellas,'traduccioningles':traduccioningles,'traduccionfrances':traduccionfrances}


    #if request.user.is_authenticated():
    #    us=PagUser.objects.get(user=request.user.username)
    #    context = {'lista':listimages[0:5],'h':hoteles,'condicion':"",'url':lista.url,'name':lista.name,
    #                'address':lista.address,'Comentarios':listcoms,'type':lista.tipo,'stars':lista.stars, 'body':lista.body,
    #                'color':us.color,'size':us.size,'user':request.user.username,'listausers':listauser}

    return render_to_response('alojamiento_id.html', context,context_instance = RequestContext(request))
    #return HttpResponse(imagelist.idHotel)

def comentarios (lista):
    dic = {}
    orderlist = []
    respuesta = ""
    for hotel in lista:
        iden = hotel.id
        try:
            comment = Comentario.objects.filter(idHotel = iden)
            dic[iden] = len(comment)
        except Comentario.DoesNotExist:
            respuesta += "No tiene comentarios"
    orderlist = sorted (dic.items(),key = itemgetter(1),reverse = True)

    return orderlist


def paginaUsuario(request , usuario ) :
    u = usuario
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


        return render_to_response('about.html' , context_instance = RequestContext(request))

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
    elif u == "accounts/invalid":
        return render_to_response('invalid_login.html')
    elif u == "/comentario":
        return HttpResponseRedirect("/comentario")


    else:
        idusu = request.user.id
        value = ""
        tamanio = ""
        tittle = ""
        selected = HotelSelect.objects.all()

        if request.method == 'POST':
            color = request.POST.get('css',"")
            tamanio = request.POST.get('size',"")
            tittle = request.POST.get('titulo',"")
            try:
                user = StyleCSS.objects.get(usuario=usuario)
                if value != "":
                    user.color = value
                if size != "":
                    user.size = tamanio
                if tittle != "":
                    user.titulo_pagina = tittle;
                    user.save()
            except StyleCSS.DoesNotExist:
                guardar = StyleCSS(usuario = usuario , titulo_pagina = titulo , color = value , size = tamanio)



    #template = get_template('user.html')
    context = {'color':value,'size':tamanio,'titulo':tittle,'selecion': selected, 'usuario': u, 'titulo': titulo} #le pasamos el objeto completo
    return render_to_response ('user.html',context,RequestContext(request))
