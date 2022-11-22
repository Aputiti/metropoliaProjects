'use strict';

const form = document.querySelector('form');
const firstName = document.getElementsByTagName('input')[0];
const lastName = document.getElementsByTagName('input')[1];
const text = document.getElementById('target');

form.addEventListener('submit', function(evt) {
  evt.preventDefault();
  text.innerText = `Your name is ${firstName.value} ${lastName.value}`;
});
