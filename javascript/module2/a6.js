'use strict';

function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

let diceRoll = rollDice();

while (diceRoll !== 6) {
  diceRoll = rollDice();
  document.querySelector('#target').innerHTML += `<li>${diceRoll}</li>`;
}
