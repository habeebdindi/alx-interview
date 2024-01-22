#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

async function starWars () {
  await request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      const characters = data.characters;
      characters.map(async (link) => {
        await request.get(link, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            const data = JSON.parse(body);
            console.log(data.name);
          }
        });
      });
    }
  });
}

starWars();
