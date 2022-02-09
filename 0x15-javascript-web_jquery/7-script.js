$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('div#character').text(data.name);
});
