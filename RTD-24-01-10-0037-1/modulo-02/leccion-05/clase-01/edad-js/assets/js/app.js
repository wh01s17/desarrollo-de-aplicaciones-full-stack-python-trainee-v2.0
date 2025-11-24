function evaluarEdad() {
    let edad = document.getElementById("edad").value;
    let mensaje = "";
    let error = "";

    edad = Number(edad);

    if (isNaN(edad)) {
        error = "Por favor ingresa un valor numérico.";
    } else if (edad <= 0) {
        error = "Edad inválida. Debe ser mayor que 0.";
    } else if (edad >= 18) {
        mensaje = "Eres mayor de edad.";
    } else {
        mensaje = "Eres menor de edad.";
    }

    if (error) {
        document.getElementById("resultado").textContent = "";
        document.getElementById("error").textContent = error;
        console.error(error);
    } else {
        document.getElementById("error").textContent = "";
        document.getElementById("resultado").textContent = mensaje;
        console.log("Edad evaluada:", edad);
        console.log("Resultado:", mensaje);
    }
}
