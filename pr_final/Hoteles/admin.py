from django.contrib import admin

# Register your models here.
from models import Hotel, Comentario , CSS , SelectedHotel

admin.site.register(Hotel)
admin.site.register(SelectedHotel)
admin.site.register(Comentario)
admin.site.register(CSS)
