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
from django.conf import settings
#from . import

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$' ,'Hoteles.views.about'),
    url(r'^alojamientos/$' , 'Hoteles.views.todos'),
    url(r'^$' , 'Hoteles.views.principal'),
    url(r'^login', 'django.contrib.auth.views.login'),
    #url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url (r'^alojamientos/(\d+)$' , 'Hoteles.views.alojamientoid'),
    url (r'^accounts/login/$','Hoteles.views.login'),
    url (r'^accounts/auth/$','Hoteles.views.auth_view'),
    url (r'^accounts/logout/$','Hoteles.views.logout'),
    url (r'^accounts/loggedin/$','Hoteles.views.loggedin'),
    url (r'^accounts/invalid/$','Hoteles.views.invalid_login'),
    #url (r'^accounts/register_success/$','Hoteles.views.register_success'),
    #url (r'^accounts/register/$','Hoteles.views.register_user'),

]
