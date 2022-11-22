'use strict';

const ul = document.getElementById('target');

const p1 = document.createElement('li');
const p2 = document.createElement('li');
const p3 = document.createElement('li');
p1.innerText = 'First item';
p2.innerText = 'Second item';
p2.classList.add('my-item');
p3.innerText = 'Third item';

ul.appendChild(p1);
ul.appendChild(p2);
ul.appendChild(p3);
