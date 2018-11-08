from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    #url(r'^pelicula/nueva/$', views.pelicula_nueva, name='pelicula_nueva'),
    url(r'^$', views.listar, name= 'listar'),
    url(r'^detalle/(?P<pk>[0-9]+)/$', views.detalle, name='detalle'),
    url(r'^podcast/nueva/$', views.nuevo, name='nuevo'),
    url(r'^podcast/(?P<pk>[0-9]+)/editar/$', views.editar, name='editar'),
    url(r'^podcast/(?P<pk>\d+)/remover/$', views.remover, name='remover'),
]
