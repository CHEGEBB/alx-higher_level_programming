#!/usr/bin/node
 
const arg1 = process.argv[2];
const arg2 = process.argv[3];

function  add (a, b) {
  return (parseInt(a) + parseInt(b));
}
console.log(add(arg1, arg2));
