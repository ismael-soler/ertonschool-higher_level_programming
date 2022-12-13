#!/usr/bin/node
const request = require('request');

const urlToCheck = process.argv[2];

request(urlToCheck, function (error, response) {
  if (error) {
    console.log('An error occurred: ' + error.message);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
