// Opción 1: asignar directamente la función al evento
// IMPORTANTE: se asigna la función SIN paréntesis.
// Si pusieras saludo(), la función se ejecutaría al cargar la página
// en vez de hacerlo cuando el usuario haga click.
document.getElementById("btnMensaje").onclick = saludo;

function saludo() {
    document.getElementById("mensaje").textContent = "Bienvenido";
}

// Opción 2: usar addEventListener (método más moderno y recomendado)
// Aquí se registra un "escuchador" de evento 'click'.
// La función flecha se ejecutará SOLO cuando ocurra el click.
document.getElementById("btnMensaje").addEventListener("click", () => {
    document.getElementById("mensaje").textContent = "Bienvenido";
});
