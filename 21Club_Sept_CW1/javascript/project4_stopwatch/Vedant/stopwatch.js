var hr = 0;
var min = 0;
var sec = 0;
var msec = 0;
var timer = false;
function start(){
    timer = true;
    stopwatch();
}

function reset(){
    timer = false;
    hr=0;
    min=0;
    sec=0;
    msec=0;
    document.getElementById("hr").innerHTML="00";
    document.getElementById("min").innerHTML="00";
    document.getElementById("sec").innerHTML="00";
    document.getElementById("msec").innerHTML="000";
}

function stopwatch(){
    if(timer == true){
        if(msec==100){
            sec=sec+1;
            msec=0;
        }
        if(sec==60){
            min=min+1;
            sec=0;
            msec=0;
        }
        if(min==60){
            hr=hr+1;
            min=0;
            sec=0;
            msec=0;
        }
        msec=msec+1;
        setTimeout("stopwatch()",10);
        document.getElementById("sec").innerHTML=sec;
        document.getElementById("msec").innerHTML=msec;
    }

}