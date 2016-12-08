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
		|3|Mechanic: Resurrection|Mechanic: Resurrection es una película franco-americana de suspenso y acción dirigida por Dennis Gansel. La película estará protagonizada por Jason Statham, Jessica Alba, Tommy Lee Jones y Michelle Ye|B|98 minutos|Acción|True|Jason Statham|1|
		Entonces puedo ver la pelicula en la lista

	Scenario: Ver lista de peliculas
		Dado que quiero ver la lista de peliculas de mi catalogo
		Cuando consulto la lista de peliculas
		Entonces puedo visualizar las peliculas en existencia y rentadas

	Scenario: Eliminar peliculas
		Dado que quiero ver la lista de peliculas de mi catalogo
		Cuando consulto la lista de peliculas
		Entonces puedo eliminar, editar o quitar el estatus de rentada a una pelicula

