#!/usr/bin/node
const args = process.argv;

if (!args[2]) {
  console.log('Missing number of size');
} else {
  for (let printalt = args[2]; printalt > 0; printalt--) {
    let Xs = '';
    for (let printanch = args[2]; printanch > 0; printanch--) {
      Xs += 'X';
    }
    console.log(Xs);
  }
}
