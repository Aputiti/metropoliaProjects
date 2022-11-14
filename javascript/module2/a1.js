'use strict';

let numList = [];

for (let i = 0; i < 5; i++) {
  numList.push(parseInt(prompt('Insert a number:')));
}

for (let i = 4; i >= 0; i--) {
  console.log(numList[i]);
}
