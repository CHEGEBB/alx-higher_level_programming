#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
