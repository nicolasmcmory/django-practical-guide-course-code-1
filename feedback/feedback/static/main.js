"use strict";

const reviewCards = document.querySelectorAll(".review-card");
const nav_buttons = document.querySelectorAll(
  "button.default-button[data-url]",
);

// Animate review cards
async function animateReviewCards() {
  reviewCards.forEach(function (card, index) {
    card.style.animationDelay = index * 0.05 + "s";
  });
}

// Add click event listeners to navigation buttons
async function navButtonClickListeners() {
  nav_buttons.forEach(function (button) {
    button.addEventListener("click", async function (event) {
      const url = event.target.dataset.url;
      if (url) {
        window.location.href = url;
      }
    });
  });
}

// Animate review cards on page  load
document.addEventListener("DOMContentLoaded", async function () {
  // Add click event listeners to navigation buttons
  await navButtonClickListeners();
  await animateReviewCards();
});
