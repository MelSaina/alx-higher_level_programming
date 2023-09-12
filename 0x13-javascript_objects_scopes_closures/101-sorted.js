#!/usr/bin/node
const { dict } = require('./101-data');

const reversedDict = {};
for (const userId in dict) {
  const occurrence = dict[userId];
  if (!reversedDict[occurrence]) {
    reversedDict[occurrence] = [];
  }
  reversedDict[occurrence].push(userId);
}

console.log(reversedDict);
