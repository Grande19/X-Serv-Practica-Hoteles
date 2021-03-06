
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import urllib
from  models import Hotel , Image 


class myContentHandler(ContentHandler):

    def __init__ (self):
        self.record=None;

        self.theContent = ""
        self.titulo=""
        self.url=""
        self.dir=""
        self.img=""
        self.tipo=""
        self.body=""
        self.recimg=None
        self.is_star=False;
        self.is_img=False;
        self.is_cat =False;
    def startElement (self, name, attrs):

        self.theContent=name
        if name =='basicData':
            self.record = Hotel(nombre="", url="",direccion="", descripcion="",tipo="")

        if name =="item":
            if attrs['name']== "SubCategoria":
                self.is_star=True;
        if name =="item":
            if attrs['name']== "Categoria":
                self.is_cat=True;
        if name =='media':
            if attrs['type']== "image":
                self.is_img=True
                self.recimg=Image(idHotel=0,img=self.record,url_I="")

    def endElement (self, name):
            if self.theContent=='body': #bien
                self.record.descripcion=self.body;
                self.record.save()

            if self.theContent=='item' and self.is_star:
                self.record.estrellas=self.tipo
                self.record.save();
                self.is_star=False;

            if self.theContent=='item' and self.is_cat:

                self.record.tipo=self.tipo
                self.record.save();
                self.is_cat=False;
            if self.theContent == 'url' and self.is_img:
                self.record.urlimagen=self.img
                self.recimg.img=self.record
                self.recimg.url_I=self.img;
                self.recimg.idHotel=self.record.id;
                self.record.save()
                self.recimg.save()
                print self.recimg.img.id
                print self.record.id
                print self.recimg.url_I
                self.is_img=False
            if self.theContent == 'title':
                self.record.nombre=self.titulo;
                self.record.save()
                #print self.titulo
            elif self.theContent == 'web':
                self.record.url=self.url
                self.record.save()
                #print self.url
            elif self.theContent == 'address':
                self.record.direccion=self.dir
                self.record.save()

                #print self.theContent
            self.theContent=""

            #record.save()
    def characters (self, chars):
        if self.theContent == 'body':
            self.body=chars
            print self.body
        if self.theContent == 'title':
            self.titulo=chars

        elif self.theContent == 'web':
            self.url=chars

        elif self.theContent == 'address':
            self.dir=chars

        elif self.theContent == 'url':
            self.img=chars
        elif self.theContent == 'item':
            self.tipo=chars
