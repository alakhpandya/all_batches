const modal_btn = document.querySelector('.lowertextbox');
const close_btn = document.getElementById('close');
const modal = document.querySelector('.txtbox');

modal_btn.addEventListener('click', () => {
    modal.classList.add('show-modal');
})

close_btn.addEventListener('click', () => {
    modal.classList.remove('show-modal');
})