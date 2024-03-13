#!/usr/bin/node
const { dict } = require('./101-data');

// Function to invert the dictionary
function invertDictionary (dict) {
  const invertedDict = {};
  for (const key in dict) {
    const value = dict[key];
    if (!invertedDict[value]) {
      invertedDict[value] = [];
    }
    invertedDict[value].push(key);
  }
  return invertedDict;
}

// Inverting the dictionary
const invertedDict = invertDictionary(dict);

// Printing the inverted dictionary
console.log(invertedDict);
