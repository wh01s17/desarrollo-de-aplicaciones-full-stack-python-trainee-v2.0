$("#show").click(function () {
    const lista = $("#lista");
    const btn = $("#show");

    lista.toggleClass("hide");
    if (lista.hasClass("hide")) {
        btn.text("Mostrar lista");
        btn.removeClass("btn-primary").addClass("btn-warning");
    } else {
        btn.text("Ocultar lista");
        btn.removeClass("btn-warning").addClass("btn-primary");
    }
});

$("#addElement").click(function () {
    const lista = $("#lista");
    const cantidad = $("#lista li").length;
    const texto = "Elemento " + (cantidad + 1);

    lista.append($("<li>").text(texto));
    lista.removeClass("rojo azul violeta verde");
    lista.addClass(randomColor());
});

$("#removeElement").click(function () {
    const lista = $("#lista");
    $("#lista li").last().remove();

    lista.removeClass("rojo azul violeta verde");
    lista.addClass(randomColor());
});

function randomColor() {
    const colors = ["rojo", "azul", "violeta", "verde"];
    const random = Math.floor(Math.random() * colors.length);
    return colors[random];
}

// necesario para activar los tooltips de bootstrap
const tooltipTriggerList = document.querySelectorAll(
    '[data-bs-toggle="tooltip"]'
);
const tooltipList = [...tooltipTriggerList].map(
    (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
);
