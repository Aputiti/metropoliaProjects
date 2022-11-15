'use strict';

let numList = [];
let userNum = parseInt(prompt('Enter a number (repeating until you enter a previously entered number):'));

while (numList.includes(userNum) === false) {
  numList.push(userNum);
  userNum = parseInt(prompt('Enter a number (repeating until you enter a previously entered number):'));
}

numList.sort((a,b) => a-b);

for (let i = 0; i < numList.length; i++) {
  console.log(numList[i]);
}
