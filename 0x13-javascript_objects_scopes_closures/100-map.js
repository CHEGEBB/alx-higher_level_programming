#!/usr/bin/node
const { list } = require('./100-data');

// Map function to create a new array with values multiplied by their index
const newList = list.map((value, index) => value * index);

// Printing the initial list and the new list
console.log(list);
console.log(newList);
