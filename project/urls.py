from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health

urlpatterns = [
    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    #----------------------------- Log In & Log out ---------------------------
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #----------------------- Direccion ----------------------------------------
    url(r'^app/', include('direcciones.urls'), name="app"),
]
