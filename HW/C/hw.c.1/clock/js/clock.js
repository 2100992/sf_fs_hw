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
const page_wrapper = $('.page-wrapper');

//функция для чтения с экрана текущего состояния таймера
function getCurrentTime() {
    let currentTime = 0;
    currentTime = currentTime + Number(unitSeconds.text());
    currentTime = currentTime + Number(tenSeconds.text()*10);
    currentTime = currentTime + Number(unitMinutes.text()*60);
    currentTime = currentTime + Number(tenMinutes.text()*600);
    return currentTime
};

//функция для записи на экран времени
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

//Изменение времени на экране.
//читаем время, изменяем его на указанную величину, пишем обратно
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

//функционал проходящий по завершению таймера
function finish() {
    h1.text('FINISH!!!');
    page_wrapper.hide()
}

//считываем клики с минутной кнопки.
//в зависимости от координаты клика прибавляем/убавляем минуты/десяткиМинут
butMin.click((e) => {
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

//считываем клики с секундной кнопки.
//в зависимости от координаты клика прибавляем/убавляем секунды/десяткиСекунд
butSec.click((e) => {
    //читаем координаты клика
    let clickX = e.clientX;
    let clickY = e.clientY;

    //вычисляем середину кнопки
    boxMiddleX = butSec.middle().x
    boxMiddleY = butSec.middle().y

    //в зависимости от попадания в определенную четверть кнопки
    //добавим или убавим необходимое число секунд
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

//читаем клики с центральной кнопки.
//если таймер не запущен, запускаем его, иначе останавливаем.
butColon.click((e) => {
    currentTime = getCurrentTime();
    if (currentTime >= 1) {
        if (countDown === false){
            countDown = true;
            dicrementTime();
        }
        else {
            countDown = false;
        }
    }
})

//функция обратного отсчета
//в функцию входим через нажатие на центральную кнопку
//если флаг countDown, то рекурсивно вызывает саму себя
//заодно 
function dicrementTime() {
    currentTime = getCurrentTime();
    if (countDown) {
        if (butColon.text() == ':'){
            butColon.text('.');
            window.setTimeout(dicrementTime, period/2);
        }
        else {
            butColon.text(':');
            if(currentTime > 1){
                changeTime(-1);
                window.setTimeout(dicrementTime, period/2);
            }
            else{
                countDown = false;
                changeTime(-1);
                finish()
            };
        };
    };
}