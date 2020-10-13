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
// {% url 'payments:popup' %}
// __payment_engineer_info.html

// 달력 생성
const js_days = document.getElementById('js-days');
function createCalendar() {
    const today = new Date();
    const startDayOfWeek = new Date(
        today.getFullYear(),
        today.getMonth(),
        1
    ).getDay();
    const endDay = new Date(
        today.getFullYear(),
        today.getMonth() + 1,
        0
    ).getDate();
    // 달력 공백 채우기
    for (let i=0; i<startDayOfWeek; ++i) {
        const li = document.createElement('li');
        js_days.appendChild(li);
    }
    // 날짜 채우기
    for (let i=1; i<=endDay; ++i) {
        const li = document.createElement('li');
        li.innerText = i;
        js_days.appendChild(li);
    }
}

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
            window.open(ENGINEER_SELECT_PAGE, 'schedule', 'width=500, height=543');
        }));
    }

    createCalendar();
}

init(); 