#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];

function writeFile (fileName, data) {
  fs.writeFile(fileName, data, 'utf8', (err) => {
    if (err) {
      return console.error(err);
    }
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    writeFile(fileName, body);
  }
});
