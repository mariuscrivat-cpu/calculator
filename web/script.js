// Doar design: butoanele nu efectueaza calcule momentan.
document.querySelectorAll('.key').forEach(function (button) {
  button.addEventListener('click', function (event) {
    event.preventDefault();
  });
});
