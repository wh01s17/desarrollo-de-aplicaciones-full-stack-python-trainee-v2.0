// Opción 1: Forma simple y fácil de leer
// Guardamos las referencias a los elementos para no repetir getElementById
const contenido = document.getElementById("contenido");
const btnToggle = document.getElementById("btnToggle");

// Cuando se hace click en el botón, se ejecuta esta función
btnToggle.onclick = function () {
    // toggle agrega la clase "oculto" si no está,
    // y la elimina si ya está presente
    // oculta / muestra el contenido
    contenido.classList.toggle("oculto");
};

// Opción 2: Forma compacta usando addEventListener
// Todo se hace en una sola línea, sin variables previas
document.getElementById("btnToggle").addEventListener("click", () => {
    // Alterna la clase "oculto" directamente sobre el elemento
    document.getElementById("contenido").classList.toggle("oculto");
});
