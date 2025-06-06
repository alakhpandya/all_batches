// const movie_title = document.getElementById('movie-title')
/* background-color = backgroundColor */
/*
movie_title.style.color = 'orange';

const movies = document.getElementsByClassName('movie-names')
for(let i = 0; i < movies.length; i++){
    movies[i].style.backgroundColor = 'orange';
}
*/
/*
const myMovie = document.querySelector('.movie-names')
myMovie.style.color = 'red'
*/

const newMovie = document.createElement('li')
const ul = document.querySelector('ul')
ul.appendChild(newMovie)

newMovie.innerText = 'X-men'
// newMovie.innerText = '<h1>X-men</h1>'
// newMovie.innerHTML = '<h1>X-men</h1>'

const title = document.querySelector('h1')
console.log(title.getAttribute('id'));
// title.setAttribute('id', 'main-title')
// newMovie.setAttribute('id', 'main-title')
newMovie.setAttribute('class', 'movie-names')
newMovie.setAttribute('class', 'orange-border')