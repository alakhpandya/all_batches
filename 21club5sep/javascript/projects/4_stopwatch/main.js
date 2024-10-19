const play_btn = document.querySelector('.play-btn')
const reset_btn = document.querySelector('.reset-btn')
const timer = document.getElementById('timer')
let hr = 0, min = 0, s = 0, ms = 0;
let timerInterval;

/*
let i = 1
const trialFunc = () => {
    console.log(`Hello - ${i}!`);
    i++;
}

const myInterval = setInterval(trialFunc, 1000);
clearInterval(myInterval)
*/
const stopwatch = () => {
    ms++;
    if (ms == 100){
        s++;
        ms = 0;
    }
    if (s == 60){
        s = 0;
        min++;
    }
    if (min == 60){
        min =0;
        hr++;
    }
    timer.innerText = `${hr.toString().padStart(2, '0')} : ${min.toString().padStart(2, '0')} : ${s.toString().padStart(2, '0')} : ${ms.toString().padStart(3, '0')}`;

}


play_btn.addEventListener('click', ()=>{

    if (play_btn.firstElementChild.classList.contains('fa-circle-play')){
        play_btn.firstElementChild.classList.remove('fa-circle-play');
        play_btn.firstElementChild.classList.add('fa-circle-pause');
        timerInterval = setInterval(stopwatch, 10);
    }
    else{
        play_btn.firstElementChild.classList.remove('fa-circle-pause');
        play_btn.firstElementChild.classList.add('fa-circle-play');
        clearInterval(timerInterval);
    }
})

reset_btn.addEventListener('click', () => {
    hr = 0;
    min = 0;
    s = 0;
    ms = 0;
    timer.innerText = `${hr.toString().padStart(2, '0')} : ${min.toString().padStart(2, '0')} : ${s.toString().padStart(2, '0')} : ${ms.toString().padStart(3, '0')}`;

})