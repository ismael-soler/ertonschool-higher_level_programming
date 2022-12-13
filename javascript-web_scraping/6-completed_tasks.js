#!/usr/bin/node
const request = require('request');

const apiURL = process.argv[2];

request.get(apiURL, (error, response, body) => {
  if (error) {
    return console.log(error);
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId]++;
      } else {
        completedTasksByUser[task.userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});
