#!/usr/bin/node

const request = require('request');

const fetchCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(JSON.parse(body).name);
      } else {
        reject(error || 'Failed to fetch data from the API');
      }
    });
  });
};

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const characterPromises = characters.map(url => fetchCharacter(url));
    Promise.all(characterPromises)
      .then(names => {
        names.forEach(name => {
          console.log(name);
        });
      })
      .catch(error => {
        console.error(error);
      });
  } else {
    console.error(error || 'Failed to fetch data from the API');
  }
});
