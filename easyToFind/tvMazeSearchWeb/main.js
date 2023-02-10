'use strict';

const form = document.querySelector('form');
const apiURL = form.action;

const section = document.getElementById('results');
const defaultMenu = document.getElementById('default');

async function fetchJson(search) {
  const answer = await fetch(apiURL + '?q=' + search);
  if (!answer.ok) {
    throw new Error(answer.statusText);
  }
  return await answer.json();
}

form.addEventListener('submit', async function(evt) {
  try {
    evt.preventDefault();
    const search = document.querySelector('#query').value;
    const series = await fetchJson(search);
    console.log(series);

    defaultMenu.remove();

    while (section.lastChild) {
      section.lastChild.remove();
    }

    if (series.length === 0) {
      const emptySearch = document.createElement('p');
      emptySearch.classList.add('defmenu');
      emptySearch.innerHTML = '&#128533;';
      section.appendChild(emptySearch);
      console.log('empty');
    }

    for (let show = 0; show < series.length; show++) {
      const ar = document.createElement('article');
      const he = document.createElement('header');
      const fig = document.createElement('figure');
      const figCap = document.createElement('figcaption');
      const para = document.createElement('p');
      const img = document.createElement('img');
      const dialog = document.createElement('dialog');
      const maina = document.createElement('a');
      const iframe = document.createElement('iframe');

      console.log('test');

      ar.classList.add('card');
      he.innerText = series[show]['show']['name'];
      figCap.innerHTML = series[show]['show']['summary'];

      if (series[show]['show']['image'] != null) {
        img.src = series[show]['show']['image']['medium'];
        img.classList.add('img');
      } else {
        img.src = 'https://via.placeholder.com/210x295/9c9c9c/FFFFFF?text=No+image';
        img.classList.add('img');
      }

      for (let i = 0; i < series[show]['show']['genres'].length; i++) {
        if ((i + 1) !== series[show]['show']['genres'].length) {
          para.innerText += series[show]['show']['genres'][i] + ' | ';
        } else {
          para.innerText += series[show]['show']['genres'][i];
        }
      }

      maina.innerText = 'Click here for more info';
      maina.classList.add('maina');
      maina.onclick = function() {
        dialog.showModal();
      };

      iframe.src = series[show]['show']['url'];
      iframe.classList.add('iframe');

      ar.appendChild(he);
      ar.appendChild(fig);
      fig.appendChild(img);
      fig.appendChild(figCap);
      ar.appendChild(para);
      dialog.appendChild(iframe);
      ar.appendChild(dialog);
      ar.appendChild(maina);

      section.appendChild(ar);

      dialog.addEventListener('click', function (event) {
        dialog.close();
      });
    }
  } catch (e) {
    console.error(e.message);
  }
});
