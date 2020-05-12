#!/usr/bin/node
const request = require('request');
const movieID = parseInt(process.argv[2]);
const movieOfSaga = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request (movieOfSaga, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200)
    {
      console.log(JSON.parse(body).title);
    }
  }
});
