const arrows = document.querySelectorAll('.arrow');

arrows.forEach(arrow => {
    arrow.addEventListener('click', () => {
        const content = arrow.nextElementSibling;
        arrow.classList.toggle('active');
        content.classList.toggle('active');
    });
});