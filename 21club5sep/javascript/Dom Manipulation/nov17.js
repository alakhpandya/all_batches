// 5 main ways to select an element from the DOM
// selecting by id:
/*
const movie_title = document.getElementById('movie-title')
console.log(movie_title)
*/

// selection by tag
/*
const movie_links = document.getElementsByTagName('a')
console.log(movie_links)
*/

// selecting by class name
/*
const movie_names = document.getElementsByClassName('movie-names')
console.log(movie_names)
*/

// query selector
/*
const h2 = document.querySelector('h2')
console.log(h2);
const all_a = document.querySelector('.all-a')
console.log(all_a);
const favourite = document.querySelector('#favourite')
console.log(favourite);
*/
// query selector all
const h2 = document.querySelectorAll('h2')
const movie_title = document.querySelectorAll('#movie-title')
// console.log(movie_title)
const movie_names = document.querySelectorAll('.movie-names')
console.log(movie_names);