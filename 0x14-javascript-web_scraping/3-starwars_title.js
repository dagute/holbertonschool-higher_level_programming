#!/usr/bin/node

const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movie;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
