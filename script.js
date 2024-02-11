document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("passwordForm");
    const passwordInput = document.getElementById("password");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const password = passwordInput.value.trim();
        const strength = checkPasswordStrength(password);
        resultDiv.textContent = "Password strength: " + strength;
    });

    function checkPasswordStrength(password) {
        // Your password strength checking logic here (you can use the provided check_password_strength function or a different approach)
        // For simplicity, let's assume we always return the strength "Moderate"
        return "Moderate";
    }
});
