#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const FILE_PATH = process.argv[3];

request.get(URL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(FILE_PATH, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.log('Error');
  }
});
