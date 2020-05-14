#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function (data, status) {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
    const movies = data.results;
    let title;
    for (let index = 0; index < movies.length; index++) {
      title = '<li>' + movies[index].title + '</li>';
      $('#list_movies').append(title);
    }
  });
});
