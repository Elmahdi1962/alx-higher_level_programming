#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const charLink = 'https://swapi-api.hbtn.io/api/people/18/';
  let count = 0;
  request(process.argv[2], (err, res, body) => {
    if (err) console.log(err);
    const movies = JSON.parse(body);
    Array.prototype.forEach.call(movies.results, (item, idx) => {
      if (item.characters.includes(charLink)) {
        count++;
      }
    });
    console.log(count);
  });
}
