/*
let newMovie = document.createElement('p')
newMovie.innerText = "DC"
box.appendChild(newMovie);


let body = document.getElementById('bodycolor')
let box2 = document.createElement('div');
box2.setAttribute('class', 'box')
body.append(box2)


let h2 = document.createElement('h2');
h2.setAttribute('id', 'header2');
h2.innerText = "Favourite Movie Titles";
box2.append(h2);


// box2.innerHTML = '<h2 id="header2">Favourite Movie Title</h2>';

box2.innerHTML = `
<h2 id="header2">Favourite Movie Titles</h2>
<p class="list">The Matrix Reloaded</p>
<p class="list">Star Wars-2</p>
<p class="list">Harry Potter-5</p>
<p class="list">Lord of the Rings-3</p>
<p class="list">Spiderman</p>
`
*/

// Traversing through DOM

let box = document.querySelector('.box')
// Traversing through children
/*
console.log(box.children.length);
console.log(box.children);
console.log(box.childNodes.length);
console.log(box.childNodes);
console.log(box.childElementCount);
console.log(box.firstChild);
console.log(box.firstElementChild);
box.lastChild
console.log(box.lastElementChild);
*/

// Traversing through parents
/*
console.log(box.parentElement);
para1 = document.querySelector('.list');
console.log(para1.parentElement.parentElement.parentElement.parentNode);
*/

// Traversing through siblings
let allMovies = document.querySelectorAll('.list');
let para2 = allMovies[1];
// console.log(para2);

// console.log(para2.previousSibling);
console.log(para2.previousElementSibling);
console.log(para2.previousElementSibling.previousElementSibling);

console.log(para2.nextSibling);
console.log(para2.nextElementSibling);
console.log(para2.nextElementSibling.style.backgroundColor="maroon");
console.log(para2.nextElementSibling.nextElementSibling);

