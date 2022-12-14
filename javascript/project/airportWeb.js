'use strict';

const button1 = document.getElementById('open1');

const afButton = document.getElementById('afButton');
const asButton = document.getElementById('asButton');
const euButton = document.getElementById('euButton');
const naButton = document.getElementById('naButton');
const saButton = document.getElementById('saButton');
const ocButton = document.getElementById('ocButton');
const anButton = document.getElementById('anButton');
const continentText = document.getElementById('continentText');
const continentFunText = document.getElementById('continentFunText');

const continentChosenButton = document.getElementById('continentChosenButton');
const countryList = document.getElementById('countryList');

const countryBox = document.getElementById('countryBox');
const countryChosenButton = document.getElementById('countryChosenButton');
const airportList = document.getElementById('airportList');

const airportBox = document.getElementById('airportBox');
const airportChosenButton = document.getElementById('airportChosenButton');
const airportDataList = document.getElementById('airportData');
const airportImage = document.getElementById('airportImg');

let userContinent = 'NA';

button1.addEventListener('click', button1Press);

afButton.addEventListener('click', afPress);
asButton.addEventListener('click', asPress);
euButton.addEventListener('click', euPress);
naButton.addEventListener('click', naPress);
saButton.addEventListener('click', saPress);
ocButton.addEventListener('click', ocPress);
anButton.addEventListener('click', anPress);

continentChosenButton.addEventListener('click', continentChosen);
countryChosenButton.addEventListener('click', countryChosen);
airportChosenButton.addEventListener('click', airportChosen)

async function getCountryList () {
  const response = await fetch(`http://localhost:3000/continent/${userContinent}`);
  const jsonResponse = await response.json();

  console.log(jsonResponse);
  console.log(jsonResponse.Name[0][0]);
  console.log(jsonResponse.Name.length);

  if (countryList.lastChild) {
    while (countryList.lastChild) {
      countryList.lastChild.remove();
    }
  }

  for (let country = 0; country < jsonResponse.Name.length; country++) {
    const countryName = document.createElement('option');
    countryName.innerText = jsonResponse.Name[country][0];

    countryList.appendChild(countryName);
  }
  /*
  if (userContinent !== 'AF' || userContinent !== "AS" || userContinent !== "EU" || userContinent !== "NA" || userContinent !== "SA" || userContinent !== "OC" || userContinent !== "AN") {
    while (countryList.lastChild) {
      countryList.lastChild.remove();
    }
  }
  */
}

async function getAirportList () {
  const response = await fetch(`http://localhost:3000/country/${countryBox.value}`);
  const jsonResponse = await response.json();

  console.log(jsonResponse);
  console.log(jsonResponse.Airport[0][0]);
  console.log(jsonResponse.Airport.length);

  if (airportList.lastChild) {
    while (airportList.lastChild) {
      airportList.lastChild.remove();
    }
  }

  for (let airport = 0; airport < jsonResponse.Airport.length; airport++) {
    const airportName = document.createElement('option');
    airportName.innerText = jsonResponse.Airport[airport][0];

    airportList.appendChild(airportName);
  }

}

async function getAirportData() {
  const response = await fetch(`http://localhost:3000/airport/${airportBox.value}/${countryBox.value}`);
  const jsonResponse = await response.json();

  console.log(jsonResponse);
  console.log(jsonResponse.DataTest[0][1]);

  airportDataList.value = '';
  airportDataList.value += 'ICAO: ' + jsonResponse.DataTest[0][1];
  airportDataList.value += '\n\nType: ' + jsonResponse.DataTest[0][2];
  airportDataList.value += '\n\nLatitude: ' + jsonResponse.DataTest[0][4];
  airportDataList.value += '\n\nLongitude: ' + jsonResponse.DataTest[0][5];
  airportDataList.value += '\n\nElevation: ' + jsonResponse.DataTest[0][6] + ' ft';
  airportDataList.value += '\n\nScheduled services: ' + jsonResponse.DataTest[0][11];
  airportDataList.value += '\n\nWikipedia: ' + jsonResponse.DataTest[0][16];

  const responseGeo = await fetch(`http://localhost:3000/geo/${jsonResponse.DataTest[0][4]}/${jsonResponse.DataTest[0][5]}`);
  const jsonResponseGeo = await responseGeo.json();

  console.log(jsonResponseGeo.Data);
  airportDataList.value += '\n\nLocation data: ' + jsonResponseGeo.Data;

  const responseImg = await fetch(`http://localhost:3000/img/${jsonResponse.DataTest[0][4]}/${jsonResponse.DataTest[0][5]}`);
  const jsonResponseImg = await responseImg.json();

  airportImage.src = jsonResponseImg.Image;
}

function button1Press() {
  console.log('opened');
}

function afPress() {
  continentText.innerText = 'Africa.';
  continentFunText.innerText = 'Africa is the continent with the most countries, 54 to be exact!';

  userContinent = 'AF';
  console.log(userContinent);
}
function asPress() {
  continentText.innerText = 'Asia.';
  continentFunText.innerText = 'Asia is the largest continent in size. Over 4.7 billion people live there!';

  userContinent = 'AS';
  console.log(userContinent);
}
function euPress() {
  continentText.innerText = 'Europe.';
  continentFunText.innerText = 'Europe houses the two smallest countries in the world!';

  userContinent = 'EU';
  console.log(userContinent);
}
function naPress() {
  continentText.innerText = 'North America.';
  continentFunText.innerText = 'North America is the only continent with all of the world\'s major biomes!';

  userContinent = 'NA';
  console.log(userContinent);
}
function saPress() {
  continentText.innerText = 'South America.';
  continentFunText.innerText = 'South America is a continent of many natural superlatives e.g. the highest waterfalls!';

  userContinent = 'SA';
  console.log(userContinent);
}
function ocPress() {
  continentText.innerText = 'Oceania.';
  continentFunText.innerText = 'Famed for its unique wildlife, Oceania is home to the Koala, Kangaroo, Kiwi bird and the Platypus!';

  userContinent = 'OC';
  console.log(userContinent);
}
function anPress() {
  continentText.innerText = 'Antarctica.';
  continentFunText.innerText = 'On Antarctica there are only research stations for scientists and no permanent settlements.';

  userContinent = 'AN';
  console.log(userContinent);
}

function continentChosen() {
  console.log('continent chosen');
  console.log(userContinent + 'chosen !!!');

  getCountryList();
}

function countryChosen() {
  console.log('country chosen');

  getAirportList();
}

function airportChosen() {
  console.log('airport chosen');

  getAirportData();
}
