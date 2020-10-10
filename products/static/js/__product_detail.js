const ship_menu_item = document.querySelectorAll('.ship-menu-item');

// 수정 - [minseok] : 검사해보니까 url 그대로 입력해서 그냥 static 형식 그대로 대입함.
const UPMENU_BUTTON = "{% static 'img/upmenu-button.png' %}";
const DOWNMENU_BUTTON = "{% static '/img/downmenu-button.png'%}";

ship_menu_item.forEach(ship_menu => ship_menu.addEventListener('click', (event) => {

    const information_button = ship_menu.querySelector('img');
    const item_in_menu = ship_menu.parentNode.querySelector('.item-in-menu');

    // UPMENU 인지 검사
    if (information_button.src.search(UPMENU_BUTTON) != -1) {
        information_button.src = DOWNMENU_BUTTON;
        if (item_in_menu)
            item_in_menu.classList.remove('show');
    } else {
        information_button.src = UPMENU_BUTTON;
        if (item_in_menu)
            item_in_menu.classList.add('show');
    }
}));