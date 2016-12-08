import datetime
from django.utils import timezone

from django import forms
from models import Pelicula, RentaPelicula


class formPeliculas(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('id_pelicula',
                  'titulo',
                  'sinopsis',
                  'clasificacion',
                  'duracion',
                  'genero',
                  'estreno',
                  'actor',
                  'status',)


class editFormPeliculas(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('id_pelicula',
                  'titulo',
                  'sinopsis',
                  'clasificacion',
                  'duracion',
                  'genero',
                  'estreno',
                  'actor',
                  'status',)


class FormRenta(forms.ModelForm):
    fecha_renta = forms.DateTimeField(initial=timezone.now)

    class Meta:
        model = RentaPelicula
        fields = ('usuario', 'pelicula', 'fecha_renta', 'fecha_entrega')
