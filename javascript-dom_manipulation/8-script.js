const helloElement = document.getElementById('hello');

fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then(data => {
    helloElement.textContent = data.hello;
  })
  .catch(error => {
    console.error('Erreur lors de la récupération du message de salutation:', error);
  });
