const butMin = $('#minutes');
const butColon = $('#colonBut');
const butSec = $('#seconds');
const h1 = $('h1');
const htmlTest = $('.htmlTest');
const tenMinutes = $('#tenMinutes');
const unitMinutes = $('#unitMinutes');
const tenSeconds = $('#tenSeconds');
const unitSeconds = $('#unitSeconds');
let period = 1000;
let countDown = false;

function getCurrentTime() {
    let currentTime = 0;
    currentTime = currentTime + Number(unitSeconds.text());
    currentTime = currentTime + Number(tenSeconds.text()*10);
    currentTime = currentTime + Number(unitMinutes.text()*60);
    currentTime = currentTime + Number(tenMinutes.text()*600);
    return currentTime
};


function changeTime(seconds) {
    currentTime = getCurrentTime();
    newTime = currentTime + Number(seconds);
    if (newTime >= 3599) {
        newTime = 3599;
        setTime(newTime);
    }
    else if(newTime >= 0 && newTime < 3599) {
        setTime(newTime);
    }
    else {
        setTime(0);
    }
}

function setTime(time) {
    console.log(`setTime(${time})`);
    tm = Math.floor(time/600);
    time = time - tm*600;
    um = Math.floor(time/60);
    time = time - um*60;
    ts = Math.floor(time/10);
    time = time - ts*10;
    us = Math.floor(time/1);

    console.log(`tm = ${tm}, um = ${um}, ts = ${ts}, us = ${us}`);

    tenMinutes.text(tm);
    unitMinutes.text(um);
    tenSeconds.text(ts);
    unitSeconds.text(us);
};

function finish() {
    h1.text('FINISH');
}

butMin.click((e) => {
    //прочтем с экрана текущее время
    let currentTime = getCurrentTime();
    //читаем координаты клика
    let clickX = e.clientX;
    let clickY = e.clientY;
    //вычисляем середину кнопки
    boxMiddleX = butMin.middle().x
    boxMiddleY = butMin.middle().y

    //в зависимости от попадания в определенную четверть кнопки
    //добавим или убавим необходимое число минут
    if ((clickY>boxMiddleY) && (clickX>boxMiddleX)) {
        changeTime(-60)
        }
    else if ((clickY>boxMiddleY) && (clickX<boxMiddleX)) {
        changeTime(-600)
        }
    else if ((clickY<boxMiddleY) && (clickX>boxMiddleX)) {
        changeTime(60)
        }
    else if ((clickY<boxMiddleY) && (clickX<boxMiddleX)) {
        changeTime(600)
        }
    }
)


butSec.click((e) => {
    //прочтем с экрана текущее время
    let currentTime = getCurrentTime();
    //читаем координаты клика
    let clickX = e.clientX;
    let clickY = e.clientY;
    //вычисляем середину кнопки
    boxMiddleX = butSec.middle().x
    boxMiddleY = butSec.middle().y

    //в зависимости от попадания в определенную четверть кнопки
    //добавим или убавим необходимое число минут
    if ((clickY>boxMiddleY) && (clickX>boxMiddleX)) {
        changeTime(-1)
        }
    else if ((clickY>boxMiddleY) && (clickX<boxMiddleX)) {
        changeTime(-10)
        }
    else if ((clickY<boxMiddleY) && (clickX>boxMiddleX)) {
        changeTime(1)
        }
    else if ((clickY<boxMiddleY) && (clickX<boxMiddleX)) {
        changeTime(10)
        }
    }
)

butColon.click((e) => {
    dicrementTime2()
    if (countDown === false){
        countDown = true;
    }
    else{
        let clickY = e.clientY;
        boxMiddleY = butColon.middle().y
        if (clickY>boxMiddleY) {
            period = period * 2
            }
        else {
            period = period / 2
        }
        console.log(`period = ${period}`)
    }
})


// let dicrementTime = setInterval(()=>{
//     currentTime = getCurrentTime()
//     if ( currentTime >= 1 && countDown) {
//         if (butColon.text() == ':'){
//             butColon.text('.');
//         }
//         else {
//             butColon.text(':');
//             changeTime(-1);
//             if (currentTime - 1 === 0) {
//                 clearInterval(dicrementTime);
//                 finish()
//             }
//         }
//     };
//     }, period/2)




function dicrementTime2() {
    if ( currentTime >= 1 && countDown) {
        if (butColon.text() == ':'){
            butColon.text('.');
        }
        else {
            butColon.text(':');
            changeTime(-1);
            if (currentTime - 1 === 0) {
                clearTimeout(dicrementTime2);
                finish()
            }
        }
    };
    window.setTimeout(dicrementTime2, period/2);
}