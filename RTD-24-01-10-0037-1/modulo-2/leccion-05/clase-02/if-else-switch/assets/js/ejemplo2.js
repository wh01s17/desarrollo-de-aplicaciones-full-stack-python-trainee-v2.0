// Función sin return: calcula y muestra el total, pero no devuelve nada
function sumarSinReturn(a, b) {
    const total = a + b;

    // Mostrar el resultado dentro de la página
    const pInterno = document.getElementById("resultado-interno-sin-return");
    pInterno.textContent = "Resultado interno (sumarSinReturn): " + total;

    // También mostrar en consola
    console.log("sumarSinReturn - total interno:", total);
}

// Función con return: calcula el total y lo devuelve
function sumarConReturn(a, b) {
    const total = a + b;
    return total;
}

// Función llamada al hacer clic en "Sumar sin return"
function botonSinReturn() {
    const a = Number(document.getElementById("num1").value);
    const b = Number(document.getElementById("num2").value);

    if (isNaN(a) || isNaN(b)) {
        alert("Por favor ingresa números válidos.");
        return;
    }

    // Llamamos a la función que no devuelve valor
    const resultado = sumarSinReturn(a, b);

    // Este párrafo muestra que el valor devuelto es undefined
    const pDevuelto = document.getElementById("resultado-devuelto-sin-return");
    pDevuelto.textContent = "Valor devuelto por sumarSinReturn: " + resultado;

    console.log("Valor devuelto por sumarSinReturn:", resultado);
}

// Función llamada al hacer clic en "Sumar con return"
function botonConReturn() {
    const a = Number(document.getElementById("num1").value);
    const b = Number(document.getElementById("num2").value);

    if (isNaN(a) || isNaN(b)) {
        alert("Por favor ingresa números válidos.");
        return;
    }

    // Aquí sí recibimos un valor de retorno
    const resultado = sumarConReturn(a, b);

    // Mostrar el resultado base
    const pResultado = document.getElementById("resultado-con-return");
    pResultado.textContent = "Resultado de sumarConReturn: " + resultado;

    // Usar el resultado en otra operación
    const resultadoMasDiez = resultado + 10;
    const pExtra = document.getElementById("resultado-extra-con-return");
    pExtra.textContent =
        "Resultado de sumarConReturn + 10: " + resultadoMasDiez;

    console.log("sumarConReturn - total:", resultado);
    console.log("sumarConReturn - total + 10:", resultadoMasDiez);
}
