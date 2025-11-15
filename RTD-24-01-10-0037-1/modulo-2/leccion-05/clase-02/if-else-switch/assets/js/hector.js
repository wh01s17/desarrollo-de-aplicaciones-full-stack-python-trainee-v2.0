function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth",
    });
}

const scrollButton = document.getElementById("scrollBtn");

window.onscroll = function () {
    if (
        document.body.scrollTop > 300 ||
        document.documentElement.scrollTop > 300
    ) {
        scrollButton.style.display = "block";
    } else {
        scrollButton.style.display = "none";
    }
};

if (scrollButton) {
    scrollButton.style.display = "none";
}
