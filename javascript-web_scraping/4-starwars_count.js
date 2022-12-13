#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];

request(apiURL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    // Converts the JSON from a string to an object
    const data = JSON.parse(body);

    const films = data.results.filter((film) => {
      return film.characters.includes('https://swapi-api.hbtn.io/api/people/18/');
    });

    console.log(films.length);
  } else {
    console.log('Error: could not retrieve character information');
  }
});
