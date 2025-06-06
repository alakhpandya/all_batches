const showHideBtn = document.querySelector('.title')
const content = document.querySelector('.content')

showHideBtn.addEventListener('click', ()=>{
    // if (content.classList.contains('show')){
    //     content.classList.remove('show')
    // }
    // else{
    //     content.classList.add('show')
    // }

    content.classList.toggle('show')
})