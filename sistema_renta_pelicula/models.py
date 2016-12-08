# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Genero(models.Model):
    tipo_genero = models.CharField(u'Tipo Genero', max_length=50)

    def __unicode__(self):
        return self.tipo_genero


class Clasificacion(models.Model):
    tipo_clasificacion = models.CharField(u'Tipo Clasificacion', max_length=3)

    def __unicode__(self):
        return self.tipo_clasificacion


class Actores(models.Model):
    nombre_actor = models.CharField(u'Nombre Actor', max_length=50)
    trayectoria = models.CharField(u'Trayectoria', max_length=1000)

    def __unicode__(self):
        return self.nombre_actor


class Pelicula(models.Model):
    id_pelicula = models.CharField(u'ID Pelicula', max_length=4)
    titulo = models.CharField(u'Titulo', max_length=75)
    sinopsis = models.CharField(u'Sinopsis', max_length=200)
    clasificacion = models.ForeignKey(Clasificacion, default=None)
    duracion = models.CharField(u'Duracion', max_length=15)
    genero = models.ForeignKey(Genero, default=None)
    estreno = models.BooleanField(u'Estreno')
    actor = models.ForeignKey(Actores, default=None)
    status = models.IntegerField(u'Estatus', default=0)

    def __unicode__(self):
        return self.titulo


class RentaPelicula(models.Model):
    fecha_renta = models.DateTimeField(u'Fecha Renta', auto_now=False, auto_now_add=True)
    usuario = models.ForeignKey(User, default=None)
    pelicula = models.ForeignKey(Pelicula, default=None)
    fecha_entrega = models.DateTimeField(u'Fecha Entrega')

    def __unicode__(self):
        return self.fecha_renta + ' ' + self.usuario


