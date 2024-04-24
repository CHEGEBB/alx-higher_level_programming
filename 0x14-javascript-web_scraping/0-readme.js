#!/usr/bin/node
const fs = require('node:fs');
fs.readFile(process.argv[2], 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
