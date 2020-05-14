#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function (data, status) {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, textStatus) {
    $('#character').text(data.name);
  });
});
