// Run after DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
  // Highlight code blocks if highlight.js is used
  if (typeof hljs !== 'undefined') {
    hljs.highlightAll();
  }

  // Select all alerts and close buttons
  const alerts = document.querySelectorAll('.alert');
  const alertCloseButtons = document.querySelectorAll('.alert__close');

  // Auto-dismiss after 5 seconds
  alerts.forEach((alert) => {
    setTimeout(() => {
      alert.style.display = 'none';
    }, 3000); // 5000ms = 5 seconds
  });

  // Manual dismiss
  alertCloseButtons.forEach((button) => {
    button.addEventListener('click', function () {
      const alert = button.closest('.alert');
      if (alert) {
        alert.style.display = 'none';
      }
    });
  });
});
