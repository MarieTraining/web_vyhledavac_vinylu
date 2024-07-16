// script.js
function showMessage() {
    var alerted = sessionStorage.getItem('alerted') || '';
    var button = document.querySelector('.student-work-button');
    
    if (alerted !== 'yes') {
        button.style.display = 'block'; // Make sure the button is visible
        button.addEventListener('click', function() {
            alert("Tohle je pouze STUDIJNÍ PROJEKT, na stránkách se pracuje, pokračuj kliknutím");
            sessionStorage.setItem('alerted', 'yes');
            button.style.display = 'none'; // Hide the button after showing the alert
        });
    } else {
        button.style.display = 'none'; // Hide the button if already alerted
    }
    
    // Log whether alerted is true or not
    console.log("Is alerted true?", alerted === 'yes');
}

