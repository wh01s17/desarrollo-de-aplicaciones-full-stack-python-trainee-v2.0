// ================================================
// script.js
// Guía completa de métodos jQuery en un solo HTML
// Incluye:
// - Lógica de cada ejercicio
// - Menú hamburguesa
// - Smooth scroll para navegación por secciones
// ================================================

$(document).ready(function () {
    // --------------------------------------------
    // 1. Menú hamburguesa + cierre al hacer clic
    // --------------------------------------------
    $("#btnMenu").on("click", function () {
        $("#sidebar").toggleClass("is-open");
    });

    // Cerrar menú al hacer clic en un enlace (en móvil)
    $("#sidebar").on("click", ".nav-link", function () {
        $("#sidebar").removeClass("is-open");
    });

    // --------------------------------------------
    // 2. Smooth scroll para enlaces internos
    // --------------------------------------------
    $('a[href^="#"]').on("click", function (e) {
        var destino = $($(this).attr("href"));
        if (destino.length) {
            e.preventDefault();
            var offset = 70; // espacio para el header
            $("html, body").animate(
                {
                    scrollTop: destino.offset().top - offset,
                },
                400
            );
        }
    });

    // --------------------------------------------
    // EJERCICIO 1: html() y text()
    // --------------------------------------------
    $("#e1_btnHtml").on("click", function () {
        $("#e1_contenido").html("<strong>Texto cambiado con html()</strong>");
    });

    $("#e1_btnText").on("click", function () {
        $("#e1_contenido").text("<strong>Texto cambiado con text()</strong>");
    });

    // --------------------------------------------
    // EJERCICIO 2: attr()
    // --------------------------------------------
    $("#e2_btnCambiarImg").on("click", function () {
        var actual = $("#e2_foto").attr("src");

        if (actual.includes("1.jpg")) {
            $("#e2_foto").attr("src", "assets/img/2.jpg");
        } else {
            $("#e2_foto").attr("src", "assets/img/7.jpg");
        }
    });

    $("#e2_btnCambiarEnlace").on("click", function () {
        $("#e2_enlace")
            .attr("href", "https://developer.mozilla.org")
            .text("Ir a MDN Web Docs");
    });

    // --------------------------------------------
    // EJERCICIO 3: val()
    // --------------------------------------------
    $("#e3_btnMostrar").on("click", function () {
        var nombre = $("#e3_nombre").val();
        if (nombre.trim() === "") {
            $("#e3_resultado").text("Por favor, ingrese un nombre.");
        } else {
            $("#e3_resultado").text(
                "Hola, " + nombre + ". Bienvenido al ejercicio 3."
            );
        }
    });

    $("#e3_btnRellenar").on("click", function () {
        $("#e3_nombre").val("Milton");
        $("#e3_resultado").text(
            "El campo se rellenó automáticamente con val()."
        );
    });

    // --------------------------------------------
    // EJERCICIO 4: width() y height()
    // --------------------------------------------
    $("#e4_btnAumentar").on("click", function () {
        var ancho = $("#e4_caja").width();
        var alto = $("#e4_caja").height();
        $("#e4_caja").width(ancho + 20);
        $("#e4_caja").height(alto + 10);
    });

    $("#e4_btnDisminuir").on("click", function () {
        var ancho = $("#e4_caja").width();
        var alto = $("#e4_caja").height();
        $("#e4_caja").width(Math.max(100, ancho - 20));
        $("#e4_caja").height(Math.max(60, alto - 10));
    });

    $("#e4_btnMedir").on("click", function () {
        var ancho = $("#e4_caja").width();
        var alto = $("#e4_caja").height();
        $("#e4_info").text(
            "Dimensiones actuales → ancho: " +
                ancho +
                " px, alto: " +
                alto +
                " px."
        );
    });

    // --------------------------------------------
    // EJERCICIO 5: insertAfter()
    // --------------------------------------------
    var e5_contador = 1;

    $("#e5_btnAgregar").on("click", function () {
        e5_contador++;
        var nuevo = $("<li>Nueva tarea " + e5_contador + "</li>");
        nuevo.insertAfter("#e5_base");
    });

    // --------------------------------------------
    // EJERCICIO 6: append()
    // --------------------------------------------
    var e6_contador = 0;

    $("#e6_btnAgregarMensaje").on("click", function () {
        e6_contador++;
        $("#e6_listaMensajes").append(
            "<li>Mensaje " + e6_contador + " agregado con append()</li>"
        );
    });

    // --------------------------------------------
    // EJERCICIO 7: prepend()
    // --------------------------------------------
    var e7_contador = 1;

    $("#e7_btnNuevoEvento").on("click", function () {
        e7_contador++;
        $("#e7_historial").prepend(
            "<li>Evento " + e7_contador + " agregado con prepend()</li>"
        );
    });

    // --------------------------------------------
    // EJERCICIO 8: after()
    // --------------------------------------------
    var e8_contador = 0;

    $("#e8_btnAgregarNota").on("click", function () {
        e8_contador++;
        $("#e8_parrafo").after(
            "<p>Nota " + e8_contador + " creada con after().</p>"
        );
    });

    // --------------------------------------------
    // EJERCICIO 9: remove()
    // --------------------------------------------
    $("#e9_listaProductos").on("click", ".e9_btnEliminar", function () {
        $(this).closest("li").remove();
    });

    // --------------------------------------------
    // EJERCICIO 10: Integrador
    // --------------------------------------------
    function e10_resetCaja() {
        $("#e10_preview").show();
        $("#e10_preview").width(260);
        $("#e10_preview").height(140);
        $("#e10_previewTexto").text("Texto inicial de ejemplo.");
        $("#e10_textoLibre").val("");
        $("#e10_ancho").val(260);
        $("#e10_alto").val(140);
    }

    // Estado inicial
    e10_resetCaja();

    $("#e10_btnHtml").on("click", function () {
        var texto = $("#e10_textoLibre").val();
        if (texto.trim() === "") {
            $("#e10_previewTexto").html("<em>No se ingresó texto.</em>");
        } else {
            $("#e10_previewTexto").html(texto);
        }
    });

    $("#e10_btnText").on("click", function () {
        var texto = $("#e10_textoLibre").val();
        if (texto.trim() === "") {
            $("#e10_previewTexto").text("Texto vacío aplicado con text().");
        } else {
            $("#e10_previewTexto").text(texto);
        }
    });

    $("#e10_btnDim").on("click", function () {
        var ancho = Number($("#e10_ancho").val());
        var alto = Number($("#e10_alto").val());

        if (isNaN(ancho) || isNaN(alto) || ancho < 100 || alto < 60) {
            alert("Ingrese dimensiones válidas (mínimo 100 x 60).");
            return;
        }

        $("#e10_preview").width(ancho);
        $("#e10_preview").height(alto);
    });

    $("#e10_btnEliminar").on("click", function () {
        $("#e10_preview").remove();
    });

    $("#e10_btnReiniciar").on("click", function () {
        // Si la caja fue eliminada, la recreamos
        if (!$("#e10_preview").length) {
            var nuevaCaja = $(
                '<div id="e10_preview" class="preview-box"><span id="e10_previewTexto"></span></div>'
            );
            $(".section-integrador .panel").eq(1).append(nuevaCaja);
        }
        e10_resetCaja();
    });
});
