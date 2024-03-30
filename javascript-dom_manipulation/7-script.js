const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

/* 
fetch(url)
  .then(res => {
    if (!res.ok) throw new Error(res.status);
    return res.json();
  })
  .then(data => {
    const movies = data.results;
    const listMovies = document.getElementById('list_movies');

    movies.map(movie => {
      const movieElement = document.createElement('li');
      movieElement.innerHTML = movie.title;
      listMovies.appendChild(movieElement);
    });
  });
 */

async function displayMoviesList() {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(res.status);
    // console.log(res.json());
    const { results } = await res.json();
    // console.log(results);
    const listMovies = document.getElementById('list_movies');
    
    // forEach loop
    /* results.forEach(movie => {
      const movieElement = document.createElement('li');
      movieElement.textContent = movie.title;
      listMovies.appendChild(movieElement)
    }); */

    // for...of loop
    for (const movie of results) {
      const movieElement = document.createElement('li');
      movieElement.textContent = movie.title;
      listMovies.appendChild(movieElement)      
    }
  } catch (e) {
    console.log('Error', e)
  }
}

displayMoviesList();
