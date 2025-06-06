const container = document.querySelector('.main-container')
let plus_icon, answer_box;
container.nextElementSibling
container.addEventListener('click', (e) => {
    plus_icon = e.target
    if (plus_icon.classList.contains('plus-icon')){
        answer_box = plus_icon.parentElement.nextElementSibling;
        // console.log(answer_box);
        /*
        if (answer_box.classList.contains('active')){
            answer_box.classList.remove('active')
        }
        else{
            answer_box.classList.add('active')
        }
        */
        answer_box.classList.toggle('active');
    }
})