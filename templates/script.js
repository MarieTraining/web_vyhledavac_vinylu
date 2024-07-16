// script.js
document.getElementById("myButton").addEventListener("click", function() {
    // Show the message
    document.getElementById("message").style.display = "block";
    
    // Enable the rest of the content
    document.querySelector('.content').style.pointerEvents = 'auto';
    document.querySelector('.content').style.opacity = '1';

    // Optionally hide the button if no longer needed
    document.getElementById("myButton").style.display = "none";
});
