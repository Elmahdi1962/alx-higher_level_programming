#!/usr/bin/node
const request = require('request');
const { json } = require('stream/consumers');

if (process.argv.length > 2) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
  request(url, (err, res, body) => {
    if (err) console.log(err);

    console.log(JSON.parse(body).title);
  });
}
