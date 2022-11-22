'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const select = document.getElementById('target');

for (let i = 0; i < students.length; i++) {
  const op = document.createElement('option');
  op.innerText = students[i].name;
  op.value = students[i].id;
  select.appendChild(op);
}
