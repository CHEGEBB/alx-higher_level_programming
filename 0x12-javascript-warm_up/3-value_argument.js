#!/usr/bin/node

const arg = process.argv[2]; // Extract the first argument passed to the script

if (arg === 0) {
  console.log('No argument');
} else {
  console.log(arg);
}
