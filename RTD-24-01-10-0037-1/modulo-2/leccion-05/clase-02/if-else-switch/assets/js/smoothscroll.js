// Smooth Scroll para todos los enlaces internos
document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (e) => {
        e.preventDefault();

        const destino = document.querySelector(link.getAttribute("href"));
        if (!destino) return;

        destino.scrollIntoView({
            behavior: "smooth",
            block: "start",
        });
    });
});
