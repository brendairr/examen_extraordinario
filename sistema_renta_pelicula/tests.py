from django.test import TestCase
from models import Pelicula
from django.test import Client
from views import nueva_pelicula,lista_peliculas
from forms import formPeliculas
# Create your tests here.

class ProbarTemplateAgregarPelicula(TestCase):

    def test_ProbarTemplateAgregarPelicula(self):
        response=self.client.get("/peliculas/nueva/")
        self.assertTemplateUsed(response,'agregarpelicula.html')

    def test_ProbarTemplatePelicula(self):
        response=self.client.get("/peliculas/")
        self.assertTemplateUsed(response,'listapelicula.html')

