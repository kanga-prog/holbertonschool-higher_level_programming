const addItemButton = document.querySelector('#add_item');

const myList = document.querySelector('.my_list');

addItemButton.addEventListener('click', function () {
  // Créer un nouvel élément <li>
  const newItem = document.createElement('li');

  // Ajouter du texte à cet élément <li>
  newItem.textContent = 'Item';

  // Ajouter l'élément <li> à la liste <ul> (élément avec la classe 'my_list')
  myList.appendChild(newItem);
});
