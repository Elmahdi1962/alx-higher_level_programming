#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');

let text = '';
if (fileA && fileB && fileC) {
  text += fs.readFileSync(fileA, (error) => {
    if (error) throw error;
  });

  text += '\n';

  text += fs.readFileSync(fileB, (error) => {
    if (error) throw error;
  });

  fs.writeFile(fileC, text, (error) => {
    if (error) throw error;
  });
}
