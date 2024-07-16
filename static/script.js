function showMessage() {
    var alerted = sessionStorage.getItem('alerted') || '';
    var button = document.querySelector('.student-work-button');
    
    if (alerted !== 'yes') {
        button.style.display = 'block'; // viditelny
        button.addEventListener('click', function() {
            //alert("Tohle je pouze STUDIJNÍ PROJEKT, na stránkách se pracuje, pokračuj kliknutím");
            sessionStorage.setItem('alerted', 'yes');
            button.style.display = 'none'; //skryty
        });
    } else {
        button.style.display = 'none';
    }
    
    console.log("Is alerted true?", alerted === 'yes'); 
}

//  showMessage - musi bezet pri naloudování skriptu
showMessage();

