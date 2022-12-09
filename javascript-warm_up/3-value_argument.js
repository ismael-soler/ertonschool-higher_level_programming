#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args[3]) {
  console.log(args[3]);
} else {
  console.log('No argument');
}
