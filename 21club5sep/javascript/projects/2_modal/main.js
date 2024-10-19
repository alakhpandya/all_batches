const btn = document.querySelector('.btn')
const chat_container = document.querySelector('.chat-container')
const exit_btn = document.querySelector('.exit-btn')

btn.addEventListener('click', ()=>{
    chat_container.classList.add('active');
})

exit_btn.addEventListener('click', ()=>{
    chat_container.classList.remove('active');
})