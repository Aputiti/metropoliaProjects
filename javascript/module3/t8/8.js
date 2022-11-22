'use strict';

const button = document.getElementById('start');
const result = document.getElementById('result');

function calc (evt) {
  const num1 = parseFloat(document.getElementById('num1').value);
  const num2 = parseFloat(document.getElementById('num2').value);
  const select = document.getElementById('operation').value;

  if (select === 'add') {
    result.innerText = (num1 + num2).toString();
  } else if (select === 'sub') {
    result.innerText = (num1 - num2).toString();
  } else if (select === 'multi') {
    result.innerText = (num1 * num2).toString();
  } else {
    result.innerText = (num1 / num2).toString();
  }
}

button.addEventListener('click', calc);
