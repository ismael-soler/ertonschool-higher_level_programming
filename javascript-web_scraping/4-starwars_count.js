#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];

request(apiURL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    // Converts the JSON from a string to an object
    const data = JSON.parse(body).results;

    const films = data.filter((film) => {
      for (const character of film.characters) {
        if (character.includes('18dsfgdfg')) {
          return true;
        }
      }
      return false;
    });
    console.log(films.length);
  } else {
    console.log('Error: could not retrieve character information');
  }
});
