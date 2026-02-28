"use strict";

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", function (event) {
    const usernameInput = document.querySelector("#id_user_name");
    const username = usernameInput.value;
    if (username === "") {
      event.preventDefault();
      // Check if error message already exists
      if (!usernameInput.parentNode.querySelector(".js-error-required")) {
        const errorMessage = document.createElement("span");
        errorMessage.textContent = " (This field is required)";
        errorMessage.className = "js-error-required";
        usernameInput.parentNode.appendChild(errorMessage);
      }
    }
  });
});
