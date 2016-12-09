import datetime
from django.shortcuts import render, redirect
from models import Pelicula, RentaPelicula
# Create your views here.
from forms import formPeliculas, editFormPeliculas, FormRenta
from django.utils import timezone



def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'listapelicula.html', {'peliculas': peliculas})


def nueva_pelicula(request):
    if request.method == 'POST':
        form = formPeliculas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/peliculas/')
    else:
        form = formPeliculas()
    return render(request, 'agregarpelicula.html', {'form': form, 'funcion': 'Nueva'})


def editar_pelicula(request, pk):
    task = Pelicula.objects.get(pk=pk)
    if request.method == 'POST':
        form = editFormPeliculas(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/peliculas/')
    else:
        form = editFormPeliculas(instance=task)
    return render(request, 'agregarpelicula.html', {'form': form, 'funcion': 'Actualizar'})


def eliminar_pelicula(request, pk):
    peli = Pelicula.objects.get(pk=pk)
    peli.delete()
    return redirect('/peliculas/')


def rentar_pelicula(request, pk):
    task = Pelicula.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormRenta(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/peliculas/')
    else:
        form = FormRenta(instance=task)
    return render(request, 'agregarrenta.html', {'form': form, 'renta': renta})
    # if request.user.is_authenticated():
    #     username = request.user
    # if request.method == 'POST':
    #     print request.method
    #     peli = Pelicula.objects.get(pk=pk)
    #     peli.status = 1
    #     print peli.status
    #     peli.save()
    #     form2 = editFormPeliculas(request.POST, instance=peli)
    #     if form2.is_valid():
    #         form2.save()
    #     if peli.estreno:
    #         d = datetime.timedelta(days=1)
    #
    #     else:
    #         d = datetime.timedelta(days=3)
    #     renta = RentaPelicula.objects.create(usuario=username, pelicula=peli, fecha_renta=timezone.now(),fecha_entrega=timezone.now() + d)
    #     form = FormRenta(request.POST, instance=renta)
    # if form.is_valid():
    #     print form.is_valid()
    #     form.save()
    #     renta.save()
    #     return redirect('/peliculas/')
    #
    # renta = RentaPelicula.objects.all()
    # return render(request, "agregarrenta.html", {'renta': renta})
