
document.addEventListener("DOMContentLoaded", function() {
    // Focus on the username input field when the page loads
    document.getElementById("username").focus();

    document.getElementById("loginBtn").addEventListener("click", login);
    document.getElementById("password").addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            login();
        }
    });
    document.getElementById("username").addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            login();
        }
    });

    function login() {
        var username = document.getElementById("username").value.trim();
        var password = document.getElementById("password").value.trim();

        if (username === "Bassant" && password === "123"||username === "Rawan" && password === "333") {
            // Redirect to the homepage or any other page after successful login
            window.location.href = "index.html";
        } else {
            alert("Invalid username or password. Please try again.");
            event.preventDefault(); // Prevent the default form submission
        }
    }
});