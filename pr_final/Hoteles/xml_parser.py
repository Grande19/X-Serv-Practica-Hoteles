from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
from datetime import datetime
from models import Hotel,User
import string
import urllib , urllib2

class ConterHandler (ContentHandler) :

    def __init(self):
        self.inBasicData = False
        self.inGeoData = False
        self.inMultimedia = False
        self.inContent = False
        self.theContent = ""
        self.extradata = False
        self.inItem = False


    def startElement (self , name , attr):
        if name == 'service':
            #self.service = normalize_whitespace(attrs.get)
