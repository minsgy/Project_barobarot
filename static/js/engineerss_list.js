const parent_engineer_pk = getElementByIdOnParent('my-engineer-pk');
const decide_buttons = document.querySelectorAll('#engineer-decide');
const please_put_time = getElementByIdOnParent('please-put-time');
const my_engineer_info = getElementByIdOnParent('my-engineer-info');

function getElementByIdOnParent(id) {
    return opener.document.getElementById(id);
}

function getElementsByIdOnChild(decide_button) {
    const engineer_info = decide_button.parentElement.querySelector('#engineer-info');
    const children = engineer_info.children;
    let elementsObj = {};
    [...children].forEach(child => {
        elementsObj[child.id] = child.innerText;
    });
    return elementsObj;
}

function getEngineerInfoElements(isParent, button) {
    // 결제 페이지의 요소들
    if (isParent) {
        return {
            image: getElementByIdOnParent('my-engineer-image'),
            name: getElementByIdOnParent('my-engineer-name'),
            number: getElementByIdOnParent('my-engineer-number'),
            affiliation: getElementByIdOnParent('my-engineer-affiliation')
        }
    }
    // 자식 페이지의 요소들
    else {
        return getElementsByIdOnChild(button);
    }
}

// 결정 버튼 눌렀을 때 호출되는 함수
// 설치기사 pk, image, name, number, affiliation(소속) 을 부모 페이지(__payment.html)로 전송
function handleDecideEngineer(event) {
    const decide_button = event.target;
    const child = getEngineerInfoElements(false, decide_button);
    const parent = getEngineerInfoElements(true, decide_button);
    const pk = child.pk;

    // 부모 페이지 기사 pk 저장
    parent_engineer_pk.value = pk;
    console.log(parent_engineer_pk);

    // 부모 페이지 기사 정보 업데이트
    parent.image.src = child.image;
    parent.name.innerText = child.name;
    parent.number.innerText = child.number;
    parent.affiliation.innerText = child.affiliation;
    if (please_put_time)
        please_put_time.parentNode.removeChild(please_put_time);
    my_engineer_info.classList.add('show');

    window.close();
}

function init() {
    // 결정 버튼을 누르면 handleDecideEngineer 함수 호출
    decide_buttons.forEach(button => button.addEventListener('click', handleDecideEngineer));
}

init();