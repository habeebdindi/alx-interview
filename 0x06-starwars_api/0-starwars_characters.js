#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function promisifiedRequest (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function starWars () {
  try {
    const body = await promisifiedRequest(url);
    const data = JSON.parse(body);
    const characters = data.characters;

    const namesPromises = characters.map(async (link) => {
      const characterBody = await promisifiedRequest(link);
      const characterData = JSON.parse(characterBody);
      return characterData.name;
    });

    const names = await Promise.all(namesPromises);
    names.forEach(name => { console.log(name); });
  } catch (error) {
    console.log(error);
  }
}

starWars();
