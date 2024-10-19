// movie-names orange-border
/*
const newMovie = document.createElement('li');
newMovie.innerText = "X-men"
const ul = document.querySelector('ul')
ul.append(newMovie)

// newMovie.setAttribute('class', 'movie-names')
// newMovie.setAttribute('class', 'orange-border')

newMovie.classList.add('movie-names')
newMovie.classList.add('orange-border')
// newMovie.classList.remove('orange-border')
console.log(newMovie.classList.contains('movie-names'))
// console.log(newMovie.classList);

// removing an entire element
ul.remove()
*/

// Traversing through the DOM

const ul = document.querySelector('ul')

// console.log(ul.parentElement);

// console.log(ul.childElementCount);
// console.log(ul.children);       // all the child ELEMENTS

// console.log(ul.childNodes);     // all the child NODES

// console.log(ul.parentNode.parentNode.parentNode.parentNode);
// console.log(ul.parentElement.parentElement.parentElement.parentElement);

// console.log(ul.firstChild);         // gives first child node
// console.log(ul.firstElementChild);       // gives first child element
// console.log(ul.lastChild);          // gives last child node
// console.log(ul.lastElementChild);       // gives last child element

// ul.children[0].style.backgroundColor = "lightgreen"

console.log(ul.previousElementSibling);     // Element
console.log(ul.previousSibling);            // Node

console.log(ul.nextElementSibling);         // Element
console.log(ul.nextSibling);                // Node