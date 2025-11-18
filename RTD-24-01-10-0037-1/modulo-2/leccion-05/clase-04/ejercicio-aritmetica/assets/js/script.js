// Ejercicio 4
const base = 4;
const altura = 7;
const area = base * altura;

console.log("Ejercicio 4:");
console.log("El area del rectangulo es: ", area);
console.log(`Detalle: Base(${base}) x Altura(${altura}) = ${area}`);

// Ejercicio 5
const edad = 17;

console.log("Ejercicio 5:");
if (edad >= 0 && edad <= 12) {
    console.log("Niño");
} else if (edad > 12 && edad <= 17) {
    console.log("Adolescente");
} else if (edad > 17) {
    console.log("Adulto");
} else {
    console.log("Edad inválida");
}

const precio = 20000;
const descuento = 5000;

function precioFinal(precio, descuento) {
    return precio - descuento;
}

console.log(`El precio final es: ${precioFinal(precio, descuento)}`);
