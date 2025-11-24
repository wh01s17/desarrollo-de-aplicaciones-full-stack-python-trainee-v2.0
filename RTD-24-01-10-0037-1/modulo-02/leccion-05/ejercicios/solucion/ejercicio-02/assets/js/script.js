// Opción 1: Usando la propiedad onclick (forma básica)
// Aquí asignamos directamente la función al evento.
// IMPORTANTE: se pasa la función SIN paréntesis.
document.getElementById("btnOcultar").onclick = ocultarImagen;
document.getElementById("btnMostrar").onclick = mostrarImagen;

function ocultarImagen() {
    // Cambiamos el display a "none" para ocultar el elemento
    document.getElementById("imagen").style.display = "none";
}

function mostrarImagen() {
    // Cambiamos el display a "block" para volver a mostrarlo
    document.getElementById("imagen").style.display = "block";
}

// Opción 2: Usando addEventListener (forma moderna y recomendada)
// Permite agregar múltiples eventos y separa mejor la lógica.
document.getElementById("btnOcultar").addEventListener("click", ocultarImagen);
document.getElementById("btnMostrar").addEventListener("click", mostrarImagen);

function ocultarImagen() {
    document.getElementById("imagen").style.display = "none";
}

function mostrarImagen() {
    document.getElementById("imagen").style.display = "block";
}

// Opción 3: Usando clases CSS (mejor práctica general)
// Aquí el JS solo agrega/quita clases, y el CSS decide cómo se ve.
const imagen = document.getElementById("imagen");
const btnOcultar = document.getElementById("btnOcultar");
const btnMostrar = document.getElementById("btnMostrar");

btnOcultar.addEventListener("click", () => {
    imagen.classList.add("oculto"); // Agregamos la clase que oculta el elemento
});

btnMostrar.addEventListener("click", () => {
    imagen.classList.remove("oculto"); // Quitamos la clase para mostrar el elemento
});
