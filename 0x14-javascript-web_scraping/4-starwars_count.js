#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let total = 0;
    for (let film of JSON.parse(body).results) {
      for (let chr of film.characters) {
        if (chr.search('/18/') > 0)
            total++;
      }
    }
    console.log(total);
  }
});
