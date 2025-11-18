const btn = document.getElementById("btnUp");

btn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

window.addEventListener("scroll", () => {
    const show = document.documentElement.scrollTop > 300;

    btn.classList.toggle("d-none", !show);
});
