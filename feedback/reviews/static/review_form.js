"use strict";

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", function (event) {
    const usernameInput = document.querySelector("#id_user_name");
    const username = usernameInput.value;
    if (username === "") {
      event.preventDefault();
      alert("Invalid username. Please enter a valid username.");
    }
  });
});
