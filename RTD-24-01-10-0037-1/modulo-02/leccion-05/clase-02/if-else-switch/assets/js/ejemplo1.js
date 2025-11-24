let opcion = 2;

if (opcion === 1) {
    console.log("Crear un usuario");
} else if (opcion === 2) {
    console.log("Editar usuario");
} else {
    console.log("Opción inválida");
}

switch (opcion) {
    case 1:
        console.log("Crear usuario");
        break;
    case 2:
        console.log("Editar usuario");
        break;
    default:
        console.log("Opción inválida");
}

// función con retorno
// function sumar(valor1, valor2, valor) {
//     return valor1 + valor2 + valor;
// }
// console.log(sumar(1, 3, 4));

// funcion anónima
// const resultado = (valor1, valor2, valor) => valor1 + valor2 + valor;
// console.log(resultado(2, 3, 4));

// funcion sin retorno
// let total = 0;
// function sumar(a, b) {
//     total = a + b;
// }
// sumar(2, 3);
// console.log(total);
