from django.contrib import admin

# Register your models here.
from models import Hotel, HotelSelect, Comentario, StyleCSS

admin.site.register(Hotel)
admin.site.register(HotelSelect)
admin.site.register(Comentario)
admin.site.register(StyleCSS)
