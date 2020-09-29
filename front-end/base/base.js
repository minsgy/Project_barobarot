const search = document.querySelector('.search'),
    search_text = search.querySelector('input');

search_text.addEventListener('blur', () => {
    search.classList.remove('focused');
});

search_text.addEventListener('click', () => {
    search.classList.add('focused');
});