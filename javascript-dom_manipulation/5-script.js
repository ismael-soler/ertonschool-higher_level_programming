#!/usr/bin/node
const header = document.querySelector('header');
const update_header = document.querySelector('#update_header');

update_header.addEventListener('click', function () {
  header.innerHTML = 'New header!!!';
});
