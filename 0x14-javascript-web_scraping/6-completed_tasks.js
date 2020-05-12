#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');
const finished = {};

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const aux = JSON.parse(body);
    for (let i = 0; i < aux.length; i++) {
      finished[aux[i].userId] = 0;
    }
    for (let j = 0; j < aux.length; j++) {
      if (aux[j].completed === true) {
        finished[aux[j].userId] += 1;
      }
    }
  }
  console.log(finished);
});
