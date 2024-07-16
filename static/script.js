// script.js
function showMessage() {
    //alert("Tohle je pouze STUDIJNÍ PROJEKT, pokračuj kliknutím");
    var button = document.querySelector('.student-work-button');
    if (button) {
        button.style.display = 'none';
    } else {
        console.error('Button element not found.');
    }
}

