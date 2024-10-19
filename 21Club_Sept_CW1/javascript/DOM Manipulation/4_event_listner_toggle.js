const show_hide_btn = document.querySelector('.box1');
const content = document.querySelector('.box2');
function show_hide(){
    if (content.classList.contains('invisible')){
        content.classList.remove('invisible');
        show_hide_btn.innerText = "Hide";
    }
    else{
        content.classList.add('invisible');
        show_hide_btn.innerText = "Reveal";
    }
}

show_hide_btn.addEventListener('click', show_hide)

// We studied content.classList.toggle('invisible') with the help of toggling navbar of blogger website project