function addItem() {
    let inputElement = document.getElementById('newItemText');
    let liElement = document.createElement('li');
    let itemsListElement = document.getElementById('items');

    liElement.innerHTML = inputElement.value;

    inputElement.value = '';
    itemsListElement.appendChild(liElement)

}
