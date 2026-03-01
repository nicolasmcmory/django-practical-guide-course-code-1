"use strict";
// Static global variables
const form = document.querySelector(".feedback-form");
const ratingRow = document.querySelector(".rating-row");
const ratingContainer = ratingRow.parentNode;
const usernameInput = document.querySelector("#id_user_name");
const reviewTextInput = document.querySelector("#id_review_text");

document.addEventListener("DOMContentLoaded", function () {
  // Validate form on submit
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    // Check if a rating is selected
    const ratingChecked = document.querySelector(
      'input[name="rating"]:checked',
    );

    let valid = true;

    // Validate username
    if (!usernameInput.value.trim()) {
      errorDisplay(usernameInput);
      valid = false;
    }

    // Validate review text
    if (!reviewTextInput.value.trim()) {
      errorDisplay(reviewTextInput);
      valid = false;
    }

    // Validate rating selection
    if (!ratingChecked) {
      errorDisplay(ratingRow);
      valid = false;
    }

    // Submit form if all validations pass
    if (valid) {
      form.submit();
    }
  });

  // Remove error message on input
  form.addEventListener("input", function (event) {
    const target = event.target;
    if (target.value.trim()) {
      const errorMessage =
        target.parentNode.querySelector(".js-error-required");
      if (errorMessage) {
        errorMessage.remove();
      }
    }
  });

  // Remove error message on rating change
  form.addEventListener("change", function (event) {
    const target = event.target;
    if (target.type === "radio" && target.name === "rating") {
      const errorMessage = ratingContainer.querySelector(".js-error-required");
      if (errorMessage) {
        errorMessage.remove();
      }
    }
  });

  console.log("Review form script loaded");
});

// Display error message if not already present
function errorDisplay(element) {
  const container = element.parentNode;
  if (!container.querySelector(".js-error-required")) {
    const errorMessage = document.createElement("div");
    errorMessage.textContent = "This field is required";
    errorMessage.className = "js-error-required";
    container.appendChild(errorMessage);
  }
}
