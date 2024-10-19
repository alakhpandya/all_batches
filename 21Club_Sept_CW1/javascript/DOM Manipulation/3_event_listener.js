let button_array = document.getElementsByClassName('inside-box');
const btn1 = button_array[0];
const btn2 = button_array[1];
const btn3 = button_array[2];
const box3 = document.getElementById('box3');

// console.log(button_array);
// console.log(btn1);
btn1.addEventListener('click', ()=>{
    alert('I love javascript!');
})

// Second way to use event listener
function showAlert(){
    alert("You love Javascript!");
}

btn2.addEventListener('click', showAlert)

let changeBgColor = () => {
    box3.style.backgroundColor = 'orange';
}
let resetBgColor = () => {
    box3.style.backgroundColor = 'transparent';
}

btn3.addEventListener('mouseenter', changeBgColor);
box3.addEventListener('mouseleave', resetBgColor);