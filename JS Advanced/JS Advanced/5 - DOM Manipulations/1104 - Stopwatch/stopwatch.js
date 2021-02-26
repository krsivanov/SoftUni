function stopwatch() {
    let timerElement = document.getElementById('time');
    let startButtonElement = document.getElementById('startBtn');
    let stopButttonElement = document.getElementById('stopBtn');
    let interval; 

    startButtonElement.addEventListener('click',function(e) {
        timerElement.textContent = '00:00';
        stopButttonElement.removeAttribute('disabled');
        e.currentTarget.setAttribute('disabled',true);
        //add timer ticking
        interval = setInterval(function() {
            let currentTime = timerElement.textContent;
            let timeArray = currentTime.split(':');
            let minutes = Number(timeArray[0]);
            let seconds = Number(timeArray[1]);

            seconds++;
            if (seconds > 59){
                minutes++;
                seconds =0;
            }

            timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2,'0')}`;
        }, 1000);
        //check if stop button is disabled
        stopButttonElement.addEventListener('click', function(e) {
            clearInterval(interval);
            e.currentTarget.setAttribute('disabled',true);
            startButtonElement.removeAttribute('disabled');
        });

    });
}