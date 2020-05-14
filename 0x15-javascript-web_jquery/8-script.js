$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status) => {
    for (const movie of data.results) {
      $('#list_movies').append($('<li></li>').text(movie.title));
    }
  });
});
