Feature: Renta de peliculas
	Como cliente del sistema de renta de peliculas
	Quiero rentar una pelicula
	Para poder relajarme despues de terminar el examen de Testing

	Scenario: Registrar renta
		Dado el siguiente formulario de registro de renta
		|fecha_renta|hora_renta|usuario|pelicula|fecha_entrega|
		|15/11/2016|18:45|juanito123|Mechanic: Resurrection|16/11/2016|
		Cuando presiono el boton Registrar renta
		Entonces puedo ver la pelicula rentada