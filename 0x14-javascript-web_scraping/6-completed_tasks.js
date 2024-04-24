#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const result = JSON.parse(body);
    const data = {};
    for (const task of result) {
      if (task.completed === true) {
        if (task.userId in data) {
          data[task.userId]++;
        } else {
          data[task.userId] = 1;
        }
      }
    }
    console.log(data);
  } else {
    console.log(error);
  }
});
