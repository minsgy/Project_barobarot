const card_wrap = document.querySelectorAll('.card-wrap');

function clickDiv(){
    card_wrap.style.border="3px solid red";
}

card_wrap.addEventListener("click", clickDiv);