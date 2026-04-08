"use strict";

const countdownTimer = document.querySelector(".countdown__header");

// Display countdown timer that resets on page reload
const countdownDuration = 60; // seconds
let remainingTime = countdownDuration;

function updateCountdown() {
  if (remainingTime >= 0) {
    const minutes = Math.floor(remainingTime / 60);
    const seconds = remainingTime % 60;
    countdownTimer.textContent = `${minutes}:${seconds.toString().padStart(2, "0")}`;
    remainingTime--;
  } else {
    clearInterval(countdownInterval);
    countdownTimer.textContent = "Time's up!";
  }
}

const countdownInterval = setInterval(updateCountdown, 1000);
