/*
let boxArray = document.querySelectorAll(".inner-box");

for(let i = 0; i < boxArray.length; i++){
    boxArray[i].addEventListener("click", ()=>{
        boxArray[i].style.backgroundColor = "yellow";
    })
}
*/

let box = document.querySelector('.box');

box.addEventListener('click', (e) => {
    // console.log(e.target);
    let element = e.target;
    element.style.backgroundColor = "yellow";
})