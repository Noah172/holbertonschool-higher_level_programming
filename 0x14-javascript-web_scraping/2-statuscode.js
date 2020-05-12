#!/usr/bin/node
const request = require('request');
const pag = process.argv[2];

request (pag, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    console.log('code:', response.statusCode);
  }
});
