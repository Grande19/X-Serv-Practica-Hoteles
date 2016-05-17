from django.contrib import admin

# Register your models here.
from models import Hotel, User, Comentario, StyleCSS

admin.site.register(Hotel)
admin.site.register(User)
admin.site.register(Comentario)
admin.site.register(StyleCSS)
