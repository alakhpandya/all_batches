let input_task = document.querySelector('input')
let add_btn = document.getElementById('add_btn')
let task_container = document.querySelector('.task-container')
let new_task
let check_btn = document.querySelectorAll('.check')
// let delete_btn = document.querySelector('.trash')

add_btn.addEventListener('click', () => {
    new_task = document.createElement('div')
    new_task.classList.add('no-class')
    new_task_text = input_task.value;
    new_task.innerHTML = `<p>${new_task_text}</p>
    <div class="task-control">
        <span class="check"><i class="fa-solid fa-check"></i></span>
        <span class="trash"><i class="fa-solid fa-trash"></i></span>
    </div>`;
    task_container.appendChild(new_task);
    input_task.value = "";
})

task_container.addEventListener('click', (e) => {
    console.log(e.target);
    if (e.target.classList.contains('fa-check') || e.target.classList.contains('check')){
        if (e.target.classList.contains('fa-check')){
            e.target.parentElement.parentElement.previousElementSibling.style.textDecoration = 'line-through';
        }
        else{
            e.target.parentElement.previousElementSibling.style.textDecoration = 'line-through';
        }
    }

    if (e.target.classList.contains('fa-trash') || e.target.classList.contains('trash')){
        if (e.target.classList.contains('fa-trash')){
            e.target.parentElement.parentElement.parentElement.remove();
        }
        else{
            e.target.parentElement.parentElement.remove();
        }
    }
})


