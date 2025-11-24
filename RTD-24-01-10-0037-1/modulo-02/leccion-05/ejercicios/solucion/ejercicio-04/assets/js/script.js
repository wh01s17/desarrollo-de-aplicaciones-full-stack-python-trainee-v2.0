// Opción 1: Usando onchange (NO es en tiempo real)
// onchange SOLO se ejecuta cuando el input pierde el foco.
// Por eso no sirve para escribir en tiempo real.
document.getElementById("inputUser").onchange = mostrarTexto;

function mostrarTexto(e) {
    // e.target es el input que disparó el evento
    // .value obtiene el texto que tiene el input
    document.getElementById("parrafo").textContent = e.target.value;
}

// Opción 2: Usando addEventListener con el evento "input"
// "input" se ejecuta cada vez que el usuario escribe en tiempo real
document.getElementById("inputUser").addEventListener("input", mostrarTexto);

function mostrarTexto(e) {
    // Actualiza el párrafo con lo que el usuario va escribiendo
    document.getElementById("parrafo").textContent = e.target.value;
}

// Opción 3: Versión recomendada y más limpia
// Guardamos referencias a los elementos para no repetir getElementById
const input = document.getElementById("inputUser");
const parrafo = document.getElementById("parrafo");

// Con el evento "input", el texto cambia en tiempo real
input.addEventListener("input", () => {
    // Usamos directamente input.value para obtener el texto
    parrafo.textContent = input.value;
});
