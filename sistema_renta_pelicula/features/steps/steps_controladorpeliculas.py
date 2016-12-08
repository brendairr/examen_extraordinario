# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select


@step(u'Dado que ingreso mi usuario "([^"]*)" y contraseña "([^"]*)"')
def dado_que_ingreso_mi_usuario_group1_y_contrasena_group2(step, usuario, passwd):
    world.driver = webdriver.Chrome('chromedriver')
    world.driver.get('http://192.168.33.10:5555/login')
    user = world.driver.find_element_by_name('username')
    contra = world.driver.find_element_by_name('password')

    user.send_keys(usuario)
    contra.send_keys(passwd)


@step(u'Cuando presiono el boton Ingresar')
def cuando_presiono_el_boton_ingresar(step):
    boton = world.driver.find_element_by_tag_name('button')
    boton.click()
    time.sleep(2)


@step(u'Entonces puedo ver el mensaje de bienvenida "([^"]*)"')
def entonces_puedo_ver_el_mensaje_de_bienvenida_group1(step, texto_esperado):
    texto = world.driver.find_element_by_tag_name('h1')
    assert texto.text == texto_esperado, \
        'El texto esperado ' + texto_esperado + ' no es igual a ' + texto.text


@step(u'Dado que presiono el boton Nueva')
def dado_que_presiono_el_boton_nueva(step):
    boton = world.driver.find_element_by_name('nueva')
    boton.click()
    time.sleep(2)


@step(u'Cuando recibo los siguientes datos')
def cuando_recibo_los_siguientes_datos(step):
    datos = step.columns
    world.driver.find_element_by_id('id_id_pelicula').send_keys(datos[0].get('id'))
    world.driver.find_element_by_id('id_titulo').send_keys(datos[1].get('titulo'))
    world.driver.find_element_by_id('id_sinopsis').send_keys(datos[2].get('sinopsis'))
    clasificacion = Select(world.driver.find_element_by_id('id_clasificacion'))
    clasificacion = clasificacion.select_by_visible_text(step.hashes.first['clasificacion'])
    world.driver.find_element_by_id('id_duracion').send_keys(datos[4].get('duracion'))
    genero = Select(world.driver.find_element_by_id('id_genero'))
    genero = genero.select_by_visible_text(step.hashes.first['genero'])
    world.driver.find_element_by_xpath('//*[@id="id_estreno"]').click()
    actor = Select(world.driver.find_element_by_id('id_actor'))
    actor = actor.select_by_visible_text(step.hashes.first['actores'])
    world.driver.find_element_by_id('id_status').send_keys(datos[8].get('estatus'))

    boton = world.driver.find_element_by_name('enviarPelicula')
    boton.click()
    time.sleep(2)


@step(u'Entonces puedo ver la pelicula en la lista')
def entonces_puedo_ver_la_pelicula_en_la_lista(step):
    world.driver.get('http://192.168.33.10:5555/peliculas')
    time.sleep(2)


@step(u'Dado que quiero ver la lista de peliculas de mi catalogo')
def dado_que_quiero_ver_la_lista_de_peliculas_de_mi_catalogo(step):
    world.driver.get('http://192.168.33.10:5555/peliculas')
    time.sleep(2)


@step(u'Cuando consulto la lista de peliculas')
def cuando_consulto_la_lista_de_peliculas(step):
    world.driver.get('http://192.168.33.10:5555/peliculas')
    time.sleep(2)


@step(u'Entonces puedo visualizar las peliculas en existencia y rentadas')
def entonces_puedo_visualizar_las_peliculas_en_existencia_y_rentadas(step):
    world.driver.get('http://192.168.33.10:5555/peliculas')
    time.sleep(2)


@step(u'Entonces puedo eliminar una pelicula rentada')
def entonces_puedo_eliminar_una_pelicula_rentada(step):
    boton = world.driver.find_element_by_name('eliminar')
    boton.click()
    time.sleep(2)


@step(u'Dado que quiero editar una pelicula de la lista')
def dado_que_quiero_editar_una_pelicula_de_la_lista(step):
    boton = world.driver.find_element_by_name('editar')
    boton.click()

    time.sleep(2)


@step(u'Cuando visualizo la pagina de edicion')
def cuando_visualizo_la_pagina_de_edicion(step):
    world.driver.get('http://192.168.33.10:5555/peliculas/2/editar')
    time.sleep(2)


@step(u'Entonces puedo editar la duracion de la pelicula')
def entonces_puedo_editar_la_duracion_de_la_pelicula(step):
    datos = step.columns
    duracion = world.driver.find_element_by_id('id_duracion').clear()
    duracion = world.driver.find_element_by_id('id_duracion').send_keys(datos[4].get('duracion'))
    boton = world.driver.find_element_by_name('enviarPelicula')
    boton.click()


@step(u'Entonces puedo quitar el estatus de rentada a una pelicula')
def entonces_puedo_quitar_el_estatus_de_rentada_a_una_pelicula(step):
    pass
