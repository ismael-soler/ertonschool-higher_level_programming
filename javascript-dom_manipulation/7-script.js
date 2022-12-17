#!/usr/bin/node
const list_movies = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(json => {
    const movies = json.results;
    movies.forEach(movie => {
      const movie_title = document.createElement('li');
      movie_title.innerHTML = movie.title;
      list_movies.appendChild(movie_title);
    });
  });
