const password = document.getElementById("password");
const checkbox = document.getElementById("checkbox");

checkbox.onchange = function(e) {
    password.type = checkbox.checked ? "text" : "password"
};