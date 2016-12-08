from django.contrib import admin
from models import Pelicula, Genero, Clasificacion, Actores, RentaPelicula

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Genero)
admin.site.register(Clasificacion)
admin.site.register(Actores)
admin.site.register(RentaPelicula)