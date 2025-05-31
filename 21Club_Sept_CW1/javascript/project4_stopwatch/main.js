const start_stop_btn = document.getElementById('start-stop');
const reset_btn = document.getElementById('reset');
const timer_digits = document.getElementById('timer-digits');
var timer_interval;
// var i = 1;

// timer variables:
var ms = 0, s = 0, min = 0, hr = 0;

const stopwatch = () => {
    // console.log(i);
    // i++;
    ms++;
    if (ms == 100){
        ms = 0;
        s++;
    
        if (s == 60){
            s = 0;
            min++;
    
            if (min == 60){
                min = 0;
                hr++;
            }
        }
    }
    timer_digits.innerText = `${hr.toString().padStart(2, '0')} : ${min.toString().padStart(2, '0')} : ${s.toString().padStart(2, '0')} : ${ms.toString().padStart(3, '0')}`;
}

// let temp = setInterval(stopwatch, 1000);
// clearInterval(temp);
// stopwatch();


start_stop_btn.addEventListener('click', () => {
    if (start_stop_btn.innerText == 'Start'){
        timer_interval = setInterval(stopwatch, 10);
        start_stop_btn.innerText = 'Pause';
    }
    else{
        clearInterval(timer_interval);
        start_stop_btn.innerText = 'Start';
    }
})

reset_btn.addEventListener('click', () => {
    ms = 0, s = 0, min = 0, hr = 0;
    timer_digits.innerText = `${hr.toString().padStart(2, '0')} : ${min.toString().padStart(2, '0')} : ${s.toString().padStart(2, '0')} : ${ms.toString().padStart(3, '0')}`;
    clearInterval(timer_interval);
})