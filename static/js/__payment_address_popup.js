const result = document.getElementById('result');
const result_help = document.getElementById('result-help');
const details = document.getElementById('details');

function handleAfterSearch(keywords, results) {
    result_help.classList.add('no-show');
    result.classList.remove('no-show');
}

function handleBeforeSearch() {
    // console.log('hihi');
}

function handleComplete() {
    // console.log('You searched');
}

function handleAfterSelect(selectedEntry) {
    const html = selectedEntry[0];
    const code5 = html.querySelector('.code5').innerText;
    const address_info = html.querySelector('.address_info').innerText;
    const full_address = `[${code5}] ${address_info}`;
    const address = document.getElementById('address');
    address.value = full_address;

    const popup = selectedEntry[0].parentNode;
    const removed = popup.querySelectorAll('.postcodify_search_result.postcode_search_result');
    removed.forEach((item) => popup.removeChild(item));
    details.focus();
}

function handleReady() {
    document.querySelector('.keyword').placeholder = '도로명 또는 지번을 입력하세요.';
}

const ADDRESS_ID = '#address';
const DETAILS_ID = '#details';

function attachAddress() {
    const address = document.querySelector(ADDRESS_ID);
    const details = document.querySelector(DETAILS_ID);
    
    const opener_address = opener.document.querySelector(ADDRESS_ID);

    opener_address.value = address.value + " " + details.value;
}