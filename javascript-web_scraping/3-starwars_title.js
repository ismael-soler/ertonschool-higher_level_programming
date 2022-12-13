#!/usr/bin/node
const request = require('request');
const moveID = process.argv[2];

request('https://swapi-api.hbtn.io/api/films/' + moveID, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log('Error: could not retrieve movie information');
  }
});
