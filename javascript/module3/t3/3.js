'use strict';
const names = ['John', 'Paul', 'Jones'];

for (let i = 0; i < names.length; i++) {
  document.querySelector('#target').innerHTML += `<li>${names[i]}</li>`;
}
