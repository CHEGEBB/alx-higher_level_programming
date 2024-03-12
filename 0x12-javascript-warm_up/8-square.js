#!/usr/bin/node

const arg = process.argv[2];
const times = parseInt(arg);
if (isNaN(times)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < times; i++) {
    console.log('X'.repeat(times));
  }
}
