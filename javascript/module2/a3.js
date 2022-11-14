'use strict';

let nameList = [];

for (let i = 0; i < 6; i++){
  nameList.push(prompt('Insert dog name:'));
}

nameList.sort();
nameList.reverse();

for (let i = 0; i < 6; i++){
  document.querySelector('#target').innerHTML += `<li>${nameList[i]}</li>`;
}
