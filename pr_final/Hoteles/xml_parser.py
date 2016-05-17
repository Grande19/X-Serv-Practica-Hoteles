from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string
import urllib , urllib2
import os.path

class CounterHandler (ContentHandler) :

    def __init__(self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.hotellist = []
        self.list = {}
        self.cont = 1

    def startElement (self , name , attrs):
        if name == 'name': #empieza cuando encuentra la etiqueta name
            self.inItem = True
            self.inContent = True
        if name == 'body' :
            self.inItem = True
            self.inContent = True
        if name == 'web' :
            self.inItem = True
            self.inContent = True
        if name == 'address' :
            self.inItem = True
            self.inContent = True
        if name == 'media' and attrs["type"] == "image" :
            self.inItem = True
        elif self.inItem:
            if name == "url" and self.cont<6 : #unicamente mostrar 5 imagenes
                self.cont += self.cont + 1
                self.inContent = True

        if name == 'item' and attrs["name"] == "Subcategoria":
            self.inItem = True
            self.inContent = True

    def endElement(self , name) :
        if name == "name":
            self.list[name] = self.theContent #aniadimos el contenido de dentro de la etiqueta al diccionario de hoteles
            self.inItem = False
            self.inContent = False
        if name == "body" :
            self.list[name] = self.theContent
            self.inItem = False
            self.inContent = False
        if name == "web" :
            self.list[name] = self.theContent
            self.inItem = False
            self.inContent = False
        if name == "address" :
            self.list[name] = self.theContent
            self.inItem = False
            self.inContent = False
        if name == "item" :
            self.list[name] = self.theContent
            self.hotellist.append(self.list) #se aniade a la lista de hoteles
            self.inItem = False
            self.inContent = False
        if name == "media":
            self.inItem = False
        elif self.inItem :
            if name == "url" :
                self.list[name] = self.theContent
                self.inContent = False

    def characters (self, chars):
        if self.inContent:
            self.theContent = chars

    def dameLista(self):
        return self.hotellist


def get():
        theParser = make_parser()
        theHandler = CounterHandler()
        theParser.setContentHandler(theHandler)

# Ready, set, go!

    xmlFile = urllib.urlopen('http://www.esmadrid.com/opendata/alojamientos_v1_es.xml')
    theParser.parse(xmlFile)
    #return ('Actualizacion completada')

print "Parse complete"
