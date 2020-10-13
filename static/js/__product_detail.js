const ship_menu_item = document.querySelectorAll('.ship-menu-item');

// 수정 - [minseok] : 검사해보니까 url 그대로 입력해서 그냥 static 형식 그대로 대입함.
const UPMENU_BUTTON = "/static/img/upmenu-button.png";
const DOWNMENU_BUTTON = "/static/img/downmenu-button.png";

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

// 수량 버튼 js
function form_btn(n) {

    var amount = document.getElementById("amount"); // 폼 선택
    amount_val = parseInt(amount.value); // 폼 값을 숫자열로 변환
    amount_val += n; // 계산
    amount.value = amount_val; // 계산된 값을 바꾼다
    if (amount_val <= 0) {
        amount.value = 1; // 만약 값이 0 이하면 1로 되돌려준다, 1보다 작은 수는 나타나지 않게하기 위해   
    } else if (amount_val > 5) {
        amount.value = 5; // 만약 값이 5 이상이면 5로 되돌려준다.
    }
}