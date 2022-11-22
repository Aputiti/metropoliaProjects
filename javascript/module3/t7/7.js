'use strict';

const trigger = document.getElementById('trigger');

function onHover (evt) {
  document.getElementById('target').src = 'img/picB.jpg';
}

function offHover (evt) {
  document.getElementById('target').src = 'img/picA.jpg';
}

trigger.addEventListener('mouseover', onHover);
trigger.addEventListener('mouseout', offHover);
