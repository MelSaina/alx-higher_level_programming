#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.error(`Error: ${error}`);
  }
});
