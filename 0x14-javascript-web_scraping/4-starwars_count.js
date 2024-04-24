#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  const results = JSON.parse(body).results;
  let count = 0;
  for (const i in results) {
    for (const j in results[i].characters) {
      if (results[i].characters[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
