function eliminarTarea(id) {
	//window.location='{% url "eliminar_mentor" pk=mentor.id %}'
	if (confirm("¿Deseas eliminar el registro?")) {
		var form = document.formTarea;
		form.id_tareas.value=id;
		form.submit();
	}

}