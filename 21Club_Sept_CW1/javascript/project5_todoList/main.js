const master_container = document.querySelector('.master-container')
const add_task_btn = document.querySelector('.btn');
const form_input = document.querySelector('input');
const task_container = document.querySelector('.task-container');

let new_task, check_btn_array, trash_btn_array, target_btn;

add_task_btn.addEventListener('click', () => {
    new_task = document.createElement('div');
    new_task.setAttribute('class', 'new-task');
    new_task.innerHTML = `<p>${form_input.value}</p>
    <div>
        <span class="icons check-btn"><i class="fa-solid fa-check"></i></span>
        <span class="icons trash-btn"><i class="fa-solid fa-trash"></i></span>
    </div>`
    task_container.appendChild(new_task);
    check_btn_array = document.querySelectorAll('.check-btn');
    trash_btn_array = document.querySelectorAll('.trash-btn');
    // console.log(check_btn_array);
})

task_container.addEventListener('click', (e) => {
    target_btn = e.target;
    if (target_btn.classList.contains('check-btn') || target_btn.classList.contains('fa-check')){
        if(target_btn.classList.contains('fa-check')){
            target_btn.parentElement.parentElement.previousElementSibling.style.textDecoration = 'line-through';
        }
        else{
            target_btn.parentElement.previousElementSibling.style.textDecoration = 'line-through';
        }
    }
    if (target_btn.classList.contains('trash-btn') || target_btn.classList.contains('fa-trash')){
        if(target_btn.classList.contains('fa-trash')){
            target_btn.parentElement.parentElement.parentElement.remove();
        }
        else{
            target_btn.parentElement.parentElement.remove();
        }
    }
})