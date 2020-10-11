/*
    달력, 시간을 선택했을 때 기능을 구현했습니다.
    작성자: 이승준
*/

// 달력 선택을 위한 변수
const days_items = document.querySelectorAll('.days li.enable');
const ACTIVE_CLASS = 'active';
let selected;

// 시간 선택을 위한 변수
const schedule = document.getElementById('js-schedule'),
    schedule_items = schedule.getElementsByTagName('li');
const ENGINEER_SELECT_PAGE = '__payment_engineer_info.html';

function init() {
    // 달력 선택 이벤트
    if (days_items) {
        days_items.forEach(item => item.addEventListener('click', () => {
            if (selected)
                selected.classList.remove(ACTIVE_CLASS);
            selected = item;
            item.classList.add(ACTIVE_CLASS);
        }));
    }

    // 시간 선택 이벤트
    if (schedule_items) {
        [...schedule_items].forEach(item => item.addEventListener('click', () => {
            window.open(ENGINEER_SELECT_PAGE, 'hi', 'width=500, height=543');
        }));
    }
}

init();