'use strict';

let numList = [];
let userNum = parseInt(prompt('Enter a number (repeating until you enter 0):'));

while (userNum !== 0) {
  numList.push(userNum);
  userNum = parseInt(prompt('Enter a number (repeating until you enter 0):'));
}

numList.sort((a,b) => a-b);
numList.reverse();

for (let i = 0; i < numList.length; i++) {
  console.log(numList[i]);
}
