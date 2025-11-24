const resultado = $("#resultado");
const num1 = Number($("#num1").val());
const num2 = Number($("#num2").val());

$("#sumar").click(function () {
    const total = num1 + num2;
    resultado.text(total);
});

$("#restar").click(function () {
    const total = num1 - num2;
    resultado.text(total);
});

$("#multiplicar").click(function () {
    const total = num1 * num2;
    resultado.text(total);
});

$("#dividir").click(function () {
    const total = num1 / num2;
    resultado.text(total);
});

$("#clean").click(function () {
    $("#num1").val("");
    $("#num2").val("");
});
