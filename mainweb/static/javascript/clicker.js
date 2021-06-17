let clickCounter = document.getElementById("counter");
let clickStart = document.getElementById("click-start");
let clickBox = document.getElementById("click-box");
let timer = document.getElementById("timer");
let result = document.getElementById("result");
let tryButton = document.getElementById("try-button");

function counter(){
    if (clickCounter.textContent == 0){
        clickStart.style.display = "none";
        let timeleft = 5;
        timer.textContent = timeleft;
        let timerFunc = setInterval(function(){
            timeleft -= 0.1;
            timer.textContent = timeleft.toFixed(1);
            if (timer.textContent == 0){
                clearInterval(timerFunc);
                clickCounter.style.display = "none";
                result.textContent = parseInt(clickCounter.textContent) / 5 + " cps";
                $.post("/home", {
                    jshighscore: clickCounter.textContent / 5
                });
                result.style.display = "block";
                tryButton.style.display = "block";
                clickBox.removeEventListener("click", counter);
                clickBox.style.pointerEvents = "none";
                clickCounter.textContent = 0;
                tryButton.addEventListener("click", function(){
                    clickStart.style.display = "block";
                    result.style.display = "none";
                    tryButton.style.display = "none";
                    clickBox.style.pointerEvents = "auto";
                    timer.textContent = "Click as fast as you can!";
                    clickBox.addEventListener("click", counter);
                })
                
            }
        },100);
        clickCounter.textContent++;
        clickCounter.style.display = "block";
    } else {
        clickCounter.textContent++;
    }
}
clickBox.addEventListener("click", counter)
