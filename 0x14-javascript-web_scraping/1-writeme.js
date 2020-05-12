#!/usr/bin/node
const fs = require('fs');
const nameFile = process.argv[2];
const fileCont = process.argv[3];

fs.writeFile(nameFile, fileCont, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
