"""pr_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from . import

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$' ,'Hoteles.views.about'),
    url(r'^alojamientos/$' , 'Hoteles.views.todos'),
    url(r'^$' , 'Hoteles.views.principal'),
    url(r'^login', 'django.contrib.auth.views.login'),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^register/$', 'Hoteles.views.new_user'),
    #url(r'^usuario/$','Hoteles.views.usuario')
    url (r'^alojamientos/(\d+)$' , 'Hoteles.views.alojamientoid'),
    #url(r'^usuario/$' , 'Hoteles.views.usuario')
    #url(r'^(.*)$','Hoteles.views.paginaUsuario')

]
