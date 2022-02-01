#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const charLink = 'https://swapi-api.hbtn.io/api/people/18/';
  request(process.argv[2], (err, res, body) => {
    if (err) console.log(err);
    const movies = JSON.parse(body);
    const result = movies.results.filter(item => item.characters.includes(charLink));
    console.log(result.length);
  });
}
