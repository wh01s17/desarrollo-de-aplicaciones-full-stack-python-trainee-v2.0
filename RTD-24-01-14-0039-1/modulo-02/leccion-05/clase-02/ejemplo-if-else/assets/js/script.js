const contador = document.getElementById("contador");
let contadorValue = Number(contador.textContent);

function sumar() {
    if (contadorValue < 20) {
        // contadorValue = contadorValue + 1
        contadorValue++;
        contador.textContent = contadorValue;
    }
}

function restar() {
    if (contadorValue > 0) {
        // contadorValue = contadorValue - 1
        contadorValue--;
        contador.textContent = contadorValue;
    }
}
