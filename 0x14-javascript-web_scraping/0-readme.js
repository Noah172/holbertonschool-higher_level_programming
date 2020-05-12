#!/usr/bin/node
const fs = require('fs');
const nameFile = process.argv[2];

fs.readFile(nameFile, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
