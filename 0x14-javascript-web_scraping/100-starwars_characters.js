#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request(character, (error, response, body) => {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  } else {
    console.log(error);
  }
});
