// Opcion 1: Manejo individual por botón
// Obtenemos el div y los botones por su ID
const contenido = document.getElementById("contenido");
const btnRojo = document.getElementById("btnRojo");
const btnAzul = document.getElementById("btnAzul");
const btnAmarillo = document.getElementById("btnAmarillo");

// Función que quita todas las clases de color
// Así aseguramos que solo un color quede activo a la vez
function limpiarColores() {
    contenido.classList.remove("rojo", "azul", "amarillo");
}

// Cada botón limpia las clases y aplica su color correspondiente
btnRojo.onclick = function () {
    limpiarColores();
    contenido.classList.add("rojo");
};

btnAzul.onclick = function () {
    limpiarColores();
    contenido.classList.add("azul");
};

btnAmarillo.onclick = function () {
    limpiarColores();
    contenido.classList.add("amarillo");
};

// Opcion 2: Delegación de eventos (más avanzada)
// Obtenemos el div una vez
const contenido = document.getElementById("contenido");

// Delegación: escuchamos todos los clicks del documento
// y filtramos solo los que ocurren sobre un botón
document.addEventListener("click", function (e) {
    // Verificamos si el elemento clickeado es un botón
    if (e.target.tagName === "BUTTON") {
        // Quitamos cualquier color previo
        contenido.classList.remove("rojo", "azul", "amarillo");

        // Obtenemos el texto del botón (Rojo, Azul, Amarillo),
        // lo pasamos a minúsculas para que coincida con las clases
        const color = e.target.textContent.toLowerCase();

        // Agregamos la clase de color al div
        contenido.classList.add(color);
    }
});
