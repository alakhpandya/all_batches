
const btn = document.getElementById('btn');
const innerBox = document.querySelector('.inside-box');
const outerBox = document.querySelector('.box');
const body = document.querySelector('body');

// Capturing Phase
/*
window.addEventListener('click', () => {
    console.log("Window Clicked!");
}, true)

body.addEventListener('click', () => {
    console.log("Body Clicked!");
}, true)

outerBox.addEventListener('click', () => {
    console.log("Outer Box Clicked!");
}, true)

innerBox.addEventListener('click', () => {
    console.log("Inner Box Clicked!");
}, true)

btn.addEventListener('click', () => {
    console.log("Button Clicked!");
})
*/
// Bubling Phase
/*
window.addEventListener('click', () => {
    console.log("Window Clicked!");
}, false)

body.addEventListener('click', () => {
    console.log("Body Clicked!");
}, false)

outerBox.addEventListener('click', (e) => {
    // e.stopPropagation();
    console.log("Outer Box Clicked!");
}, false)

innerBox.addEventListener('click', () => {
    console.log("Inner Box Clicked!");
}, false)

btn.addEventListener('click', () => {
    console.log("Button Clicked!");
}, false)
*/

// use of stopPropagation & stopImmediatePropagation
window.addEventListener('click', (e) => {
    e.stopPropagation();
    console.log("Event is stopped at 'window'");
}, true)

btn.addEventListener('click', () => {
    alert("You clicked on the button!");
})