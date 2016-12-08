from django.conf.urls import url
from views import lista_peliculas, nueva_pelicula, editar_pelicula, eliminar_pelicula, rentar_pelicula


urlpatterns = [
    url(r'^$', lista_peliculas, name="lista_peliculas"),
    url(r'^nueva/$', nueva_pelicula, name="nueva_pelicula"),
    url(r'^(?P<pk>[0-9]+)/editar/$', editar_pelicula, name="editar_pelicula"),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', eliminar_pelicula, name="eliminar_pelicula"),
    url(r'^(?P<pk>[0-9]+)/rentar/$', rentar_pelicula, name="rentar_pelicula"),
]
