#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data.toString('utf-8'));
});
