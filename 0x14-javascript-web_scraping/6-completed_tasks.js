#!/usr/bin/node
const request = require('request');
const pag = process.argv[2];

request(pag, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const bod = JSON.parse(body);
    const di = {};
    for (const toDo of bod) {
      if (toDo.completed) {
        if (di[toDo.userId]) {
          di[toDo.userId] += 1;
        } else {
          di[toDo.userId] = 1;
        }
      }
    }
    console.log(di);
  }
});
