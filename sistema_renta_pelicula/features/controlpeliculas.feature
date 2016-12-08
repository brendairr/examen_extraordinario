Feature: Agregar peliculas
	Como Administrador del Sistema de Renta de Peliculas
	Quiero agregar peliculas a mi catalogo
	Para mantener mi inventario de peliculas actualizado

	Scenario: Ingresar al sistema
		Dado que ingreso mi usuario "admin" y contraseña "root1234"
		Cuando presiono el boton Ingresar
		Entonces puedo ver el mensaje de bienvenida "Catálogo de Películas"

	Scenario: Agregar nueva pelicula
		Dado que presiono el boton Nueva
		Cuando recibo los siguientes datos
		|id|titulo|sinopsis|clasificacion|duracion|genero|estreno|actores|estatus|
		|10|prueba_v1000|prueba de escenarios eliminar, editar|A|8 minutos|Infantil|False|Brandon Hall|1|
		Entonces puedo ver la pelicula en la lista

	Scenario: Ver lista de peliculas
		Dado que quiero ver la lista de peliculas de mi catalogo
		Cuando consulto la lista de peliculas
		Entonces puedo visualizar las peliculas en existencia y rentadas

	Scenario: Eliminar peliculas
		Dado que quiero ver la lista de peliculas de mi catalogo
		Cuando consulto la lista de peliculas
		Entonces puedo eliminar una pelicula rentada

	Scenario: Editar peliculas
		Dado que quiero editar una pelicula de la lista
		Cuando visualizo la pagina de edicion
		Entonces puedo editar la duracion de la pelicula
		|id|titulo|sinopsis|clasificacion|duracion|genero|estreno|actores|estatus|
		|1|prueba|examen testing|C|3 dias|Terror|True|Alejandro Mauricio González|0|

    Scenario: Cambiar status de peliculas
		Dado que quiero ver la lista de peliculas de mi catalogo
		Cuando consulto la lista de peliculas
		Entonces puedo quitar el estatus de rentada a una pelicula

