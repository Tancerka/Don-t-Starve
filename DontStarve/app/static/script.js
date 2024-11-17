// script.js

document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Miejsce na integrację z backendem (Python Django)
    console.log(`Wprowadzone dane: użytkownik: ${username}, hasło: ${password}`);

    // Przykładowa walidacja danych (do zastąpienia backendem)
    if (username === "admin" && password === "1234") {
        alert("Logowanie pomyślne!");
        window.location.href = "/dashboard";
    } else {
        document.getElementById("error-message").textContent = "Nieprawidłowa nazwa użytkownika lub hasło.";
    }
});
