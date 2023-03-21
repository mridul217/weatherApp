const form = document.querySelector('form');
const input = document.querySelector('input[name="city"]');
const errorMessage = document.createElement('p');
errorMessage.classList.add('error-message');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const city = input.value;
  const response = await fetch(`/weather/${city}`);
  const data = await response.json();
  if (data.error) {
    errorMessage.textContent = data.error;
    form.appendChild(errorMessage);
  } else {
    errorMessage.remove();
  }
});
