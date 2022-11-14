'use strict';

let nameList = [];
const pNum = parseInt(prompt('How many participants?'));

for (let i = 0; i < pNum; i++){
  nameList.push(prompt('Insert participant name:'));
  document.querySelector('#target').innerHTML += `<li>${nameList[i]}</li>`;
}
