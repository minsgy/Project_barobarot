/*
    달력, 시간을 선택했을 때 기능을 구현했습니다.
    작성자: 이승준
*/

// django 로 POST 요청 전송 함수
function postData(url = '', data = {}) {
    var headers = new Headers();
    headers.append('X-CSRFToken', CSRF_TOKEN);
    headers.append('Accept', 'application/json, text/plain, */*');
    headers.append('Content-Type', 'application/x-www-form-urlencoded');

    return fetch(url,
        {
            method: 'post',
            headers: headers,
            credentials: 'include',
            body: JSON.stringify(data)
        }
    );
}

// 달력, 시간 선택 시 css 에서 활성화 시켜줄 때 쓰는 클래스 이름
const ACTIVE_CLASS = 'active';

// 달력 선택을 위한 변수
let selected_calendar;

// 시간 선택을 위한 변수
const schedule = document.getElementById('js-schedule'),
    schedule_items = schedule.getElementsByTagName('li');
let selected_schedule;
// {% url 'payments:popup' %}
// __payment_engineer_info.html

// 숫자를 두 자리 맞춰서 포맷팅
function formatDate(number) {
    return number < 10 ? `0${number}` : number;
}

// 달력 생성
const js_days = document.getElementById('js-days');
function createCalendar() {
    const today = new Date();
    const day = today.getDate();
    const month = today.getMonth();
    const year = today.getFullYear();
    const startDayOfWeek = new Date(
        year,
        month,
        1
    ).getDay();
    const endDay = new Date(
        year,
        month,
        0
    ).getDate();
    // 달력 공백 채우기
    for (let i = 0; i < startDayOfWeek; ++i) {
        const li = document.createElement('li');
        js_days.appendChild(li);
    }
    // 날짜 채우기
    for (let i = 1; i <= endDay; ++i) {
        const li = document.createElement('li');
        // 2020-10-10
        if (i > day) {
            li.classList.add('enable');
            const option = document.createElement('option');
            option.value = `${year}-${formatDate(month + 1)}-${formatDate(i)}`;
            option.innerText = i;
            li.appendChild(option);
        } else {
            li.innerText = i;
        }
        js_days.appendChild(li);
    }
}

function init() {
    createCalendar();

    // 달력 선택 이벤트
    const days_items = document.querySelectorAll('#js-days>li.enable');
    if (days_items) {
        days_items.forEach(item => item.addEventListener('click', () => {
            if (selected_calendar) {
                selected_calendar.classList.remove(ACTIVE_CLASS);
                selected_calendar.querySelector('option').name = '';
            }
            selected_calendar = item;
            item.classList.add(ACTIVE_CLASS);
            item.querySelector('option').name = 'date';
        }));
    }

    // 시간 선택 이벤트
    if (schedule_items) {
        [...schedule_items].forEach(item => item.addEventListener('click', () => {
            if (selected_schedule) {
                selected_schedule.classList.remove(ACTIVE_CLASS);
                selected_schedule.querySelector('option').name = '';
            }
            selected_schedule = item;
            item.classList.add(ACTIVE_CLASS);
            item.querySelector('option').name = 'date';
            const selected_data = {
                date: document.querySelector('#js-days>li.active>option').value,
                time: document.querySelector('#js-schedule>li.active>option').value
            };
            // 선택된 날짜, 시간 django 로 post 요청
            postData(ENGINEER_SELECT_PAGE, selected_data).then(response => {
                const blob = response.blob();
                blob.then(b => {
                    const url = URL.createObjectURL(b);
                    window.open(url, 'schedule', 'width=500, height=543');
                })
            });
        }));
        // window.open(ENGINEER_SELECT_PAGE, 'schedule', 'width=500, height=543');
    }
}

init(); 