// script.js
function showMessage() {
    //alert("Tohle je pouze STUDIJNÍ PROJEKT, na stránkách se pracuje, pokračuj kliknutím");
    var button = document.querySelector('.student-work-button');
    if (button) {
        button.style.display = 'none';
    } else {
        console.error('Button element not found.');
    }
}

