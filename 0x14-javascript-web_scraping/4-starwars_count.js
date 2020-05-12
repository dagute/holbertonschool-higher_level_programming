#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let total = 0;
    for (const film of JSON.parse(body).results) {
      for (const wa of film.characters) {
        if (wa.search('/18/') > 0) {
          total++;
        }
      }
    }
    console.log(total);
  }
});
