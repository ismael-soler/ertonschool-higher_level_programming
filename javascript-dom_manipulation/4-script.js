#!/usr/bin/node
const add_item = document.getElementById('add_item');
const my_list = document.getElementsByClassName('my_list');

add_item.addEventListener('click', function () {
  var newItem = document.createElement('li');
  newItem.innerHTML = 'Item';
  my_list[0].appendChild(newItem);
});
