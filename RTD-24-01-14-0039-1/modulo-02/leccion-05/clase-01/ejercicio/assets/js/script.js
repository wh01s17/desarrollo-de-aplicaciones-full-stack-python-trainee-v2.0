// Cambia la clase del elemento para modificar su color de fondo
function changeBackground() {
    // Referencia al elemento que se va a modificar
    const contentRef = document.getElementById("onclickEvent");

    // Lista de clases que representan colores
    const colors = ["rojo", "azul", "amarillo", "verde"];

    // Elimina cualquiera de las clases de color que ya tenga aplicadas
    contentRef.classList.remove("rojo", "azul", "amarillo", "verde");

    // Genera un índice aleatorio basado en la cantidad de colores disponibles
    const random = Math.floor(Math.random() * colors.length);

    // Agrega una clase aleatoria al elemento
    contentRef.classList.add(colors[random]);
}

// Alterna (agrega o quita) la clase que cambia el color del texto
function changeColor() {
    // Obtiene el párrafo al que se le aplicará la clase
    const parrafoRef = document.getElementById("ondblclickEvent");

    // toggle agrega la clase si no está, o la quita si ya está aplicada
    parrafoRef.classList.toggle("textoRojo");
}

// Cambia el texto cuando el mouse pasa por encima del elemento (onmouseover)
function welcomeMesasge() {
    // Referencia al elemento cuyo texto cambiará
    const textRef = document.getElementById("mouseEvent");

    // Cambia el contenido del texto a "Bienvenido"
    textRef.textContent = "Bienvenido";
}

// Restaura el texto original cuando el mouse sale del elemento (onmouseout)
function resetMessage() {
    // Referencia al elemento afectado
    const textRef = document.getElementById("mouseEvent");

    // Restaura el texto a "Hola"
    textRef.textContent = "Hola";
}

// Configura los eventos de focus y blur para un input
function setupInputEvents() {
    // Referencia al input que recibirá los eventos
    const input = document.getElementById("focusEvent");

    // Evento que se activa cuando el usuario hace clic o enfoca el input
    input.onfocus = function () {
        // Agrega una clase que puede servir para resaltar el input
        input.classList.add("focus");
    };

    // Evento que se activa cuando el input pierde el foco
    input.onblur = function () {
        // Quita la clase para volver al estilo normal
        input.classList.remove("focus");
    };
}

// Inicializa los eventos del input al cargar el script
setupInputEvents();
