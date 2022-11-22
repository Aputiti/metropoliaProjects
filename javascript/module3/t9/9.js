'use strict';

const button = document.getElementById('start');
const result = document.getElementById('result');

function calc (evt) {
  const input = document.getElementById('calculation').value;

  if (input.includes('+')) {
    let part = input.split('+');
    result.innerText = (parseInt(part[0]) + parseInt(part[1])).toString();
  } else if (input.includes('-')) {
    let part = input.split('-');
    result.innerText = (parseInt(part[0]) - parseInt(part[1])).toString();
  } else if (input.includes('*')) {
    let part = input.split('*');
    result.innerText = (parseInt(part[0]) * parseInt(part[1])).toString();
  } else if (input.includes('/')) {
    let part = input.split('/');
    result.innerText = (parseInt(part[0]) / parseInt(part[1])).toString();
  } else {
    result.innerText = 'Please include only one of the following: +, -, * or /';
  }
}

button.addEventListener('click', calc);
