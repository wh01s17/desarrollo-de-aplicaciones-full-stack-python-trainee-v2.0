// ===========
// VARIABLES
// ===========

let nombre = "wh01s17";
let edad = 32;
let estadoActivo = true;

console.log("Ejercicio de variables:");
console.log(nombre, edad, estadoActivo);

// typeof
console.log(typeof nombre);
console.log(typeof edad);
console.log(typeof estadoActivo);
console.log("----------------------");

// =============
// EJERCICIO 1
// =============

let nombreUsuario = "wh01s17";
let edadUsuario = 32;
let tienePemiso = false;
const precioProducto = 1990;

console.log("Ejercicio 1");
console.log(nombreUsuario, edadUsuario, tienePemiso, precioProducto);
console.log("----------------------");

// =============
// EJERCICIO 2
// =============

// const curso = "JavaScript";
// let alumnos = 25;
// let esOnline = false;

// console.log("Ejercicio 1");
// console.log(
//     "El curso " +
//         curso +
//         "tiene " +
//         alumnos +
//         " y" +
//         `${esOnline ? " es online" : " es offline"}`
// );

// =============
// EJERCICIO 3
// =============

const curso = "JavaScript";
let alumnos = 25;
let esOnline = false;

console.log("Ejercicio 1");

console.log(
    `El curso ${curso} tiene ${alumnos} alumnos y ${
        esOnline ? "es online" : "es offline"
    }`
);
