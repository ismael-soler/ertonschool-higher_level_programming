#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];

request(apiURL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    // Converts the JSON from a string to an object
    const data = JSON.parse(body);
    let counter = 0;

    // Check
    data.results.forEach(movie => {
      if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        counter++;
      }
    });
    console.log(counter);
  } else {
    console.log('Error: could not retrieve movie information');
  }
});
