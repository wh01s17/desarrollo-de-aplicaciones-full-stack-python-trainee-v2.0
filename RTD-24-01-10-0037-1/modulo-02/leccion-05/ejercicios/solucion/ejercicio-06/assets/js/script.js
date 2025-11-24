const tarjeta = document.getElementById("tarjeta");
const contador = document.getElementById("contador");

// Función aritmética: sumar dos números
function sumar(a, b) {
    return a + b;
}

let clicks = 0;

tarjeta.onclick = function () {
    // Alternar entre activo e inactivo
    tarjeta.classList.toggle("activo");
    tarjeta.classList.toggle("inactivo");

    // Actualizar el contador usando la función aritmética
    clicks = sumar(clicks, 1);

    contador.textContent = "Clicks: " + clicks;
};
