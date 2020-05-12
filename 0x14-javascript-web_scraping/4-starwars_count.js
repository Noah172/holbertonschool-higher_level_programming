#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    const bod = JSON.parse(body);
    let wedge = 0;
    for (const film of bod.results) {
      for (const antilles of film.characters) {
        if (antilles.endsWith('/18/')) {
          wedge += 1;
        }
      }
    }
    console.log(wedge);
  }
});
