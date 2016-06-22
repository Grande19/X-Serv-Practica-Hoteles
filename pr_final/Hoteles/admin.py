from django.contrib import admin

# Register your models here.
from models import Hotel, Usuarios, Comentario, StyleCSS

admin.site.register(Hotel)
admin.site.register(Usuarios)
admin.site.register(Comentario)
admin.site.register(StyleCSS)
