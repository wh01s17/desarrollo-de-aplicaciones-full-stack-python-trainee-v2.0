// Seleccionamos todos los <li> dentro del elemento con id="lista"
// querySelectorAll devuelve una NodeList con todos los elementos encontrados
const lista = document.querySelectorAll("#lista li");

// Obtenemos el botón que activará la numeración
const btnNumerar = document.getElementById("btnNumerar");

// Evento al hacer click en el botón
btnNumerar.onclick = function () {
    // Recorremos cada elemento <li> usando forEach
    // "li" es el elemento actual
    // "index" es la posición (comienza desde 0)
    lista.forEach((li, index) => {
        // El número mostrado debe partir en 1, por eso sumamos 1 al índice
        const numero = index + 1;

        // Usamos un operador ternario para saber si es par o impar
        // Si el número es divisible por 2 "par", si no "impar"
        const tipo = numero % 2 === 0 ? "par" : "impar";

        // Actualizamos el texto del <li>
        li.textContent = `${numero}. Item (${tipo})`;
    });
};
