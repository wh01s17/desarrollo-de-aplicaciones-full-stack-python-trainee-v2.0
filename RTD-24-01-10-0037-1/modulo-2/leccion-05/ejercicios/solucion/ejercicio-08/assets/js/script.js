// Obtenemos el input donde el usuario escribe el comentario
const input = document.getElementById("comentarioInput");

// Obtenemos el botón que agregará el comentario
const boton = document.getElementById("agregarBtn");

// Obtenemos la lista donde se mostrarán los comentarios agregados
const lista = document.getElementById("listaComentarios");

// Cuando el usuario hace clic en el botón...
boton.onclick = function () {
    // Obtenemos el texto del input y eliminamos espacios al inicio y al final
    const texto = input.value.trim();

    // Si el input está vacío, salimos de la función (no se agrega nada)
    if (texto === "") return;

    // Creamos un nuevo elemento <li> para agregar a la lista
    const nuevoComentario = document.createElement("li");

    // Le asignamos el texto que escribió el usuario
    nuevoComentario.textContent = texto;

    // Insertamos el nuevo <li> dentro de la lista <ul> o <ol>
    lista.appendChild(nuevoComentario);

    // Limpiamos el input después de agregar el comentario
    input.value = "";
};
