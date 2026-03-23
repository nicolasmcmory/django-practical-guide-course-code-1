// Get commentForm element
const commentForm = document.getElementById("comment-form");
// clone node from error-template
const errorTemplate = document
  .getElementById("error-template")
  .content.cloneNode(true);

// Helper: remove error message directly after a field
function clearFieldError(field) {
  const next = field.nextElementSibling;
  if (next && next.classList.contains("text-danger")) {
    next.remove();
  }
}

// Clear errors dynamically as user types
const userName = document.getElementById("id_user_name");
const userEmail = document.getElementById("id_user_email");
const content = document.getElementById("id_content");

userName.addEventListener("input", () => clearFieldError(userName));
userEmail.addEventListener("input", () => clearFieldError(userEmail));
content.addEventListener("input", () => clearFieldError(content));

// Validate fields on submit
commentForm.addEventListener("submit", function (event) {
  console.log("Validating comment form...");

  // Clear all remaining errors
  document.querySelectorAll(".text-danger").forEach((el) => el.remove());

  let hasError = false;

  // Validate user name
  if (userName.value.trim() === "") {
    const error = errorTemplate.cloneNode(true).querySelector(".text-danger");
    error.textContent = "Name is required.";
    userName.insertAdjacentElement("afterend", error);
    hasError = true;
  }

  // Validate user email
  if (userEmail.value.trim() === "") {
    const error = errorTemplate.cloneNode(true).querySelector(".text-danger");
    error.textContent = "Email is required.";
    userEmail.insertAdjacentElement("afterend", error);
    hasError = true;
  } else if (!/\S+@\S+\.\S+/.test(userEmail.value)) {
    const error = errorTemplate.cloneNode(true).querySelector(".text-danger");
    error.textContent = "Enter a valid email address.";
    userEmail.insertAdjacentElement("afterend", error);
    hasError = true;
  }

  // Validate content
  if (content.value.trim() === "") {
    const error = errorTemplate.cloneNode(true).querySelector(".text-danger");
    error.textContent = "Comment content is required.";
    content.insertAdjacentElement("afterend", error);
    hasError = true;
  }

  // If there are errors, prevent form submission
  if (hasError) {
    event.preventDefault();
  }
});
