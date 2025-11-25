const resultado = $("#resultado");
const num1 = Number($("#num1").val());
const num2 = Number($("#num2").val());
let total = 0;

$("#sumar").click(function () {
    total = num1 + num2;
    resultado.text(total);
});

$("#restar").click(function () {
    total = num1 - num2;
    resultado.text(total);
});

$("#multiplicar").click(function () {
    total = num1 * num2;
    resultado.text(total);
});

$("#dividir").click(function () {
    total = num1 / num2;
    resultado.text(total);
});

$("#clean").click(function () {
    $("#num1").val("");
    $("#num2").val("");
    total = 0;
});
