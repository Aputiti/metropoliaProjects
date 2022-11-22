'use strict';

const button = document.querySelector('button');

function bPressed (evt) {
  alert('Button clicked');
}

button.addEventListener('click', bPressed);
