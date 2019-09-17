const butMin = $('#minutes')
const butColon = $('#colonBut')
const butSec = $('seconds')
const div = $('div')
const container = $('.container')
const h1 = $('h1')
const htmlTest = $('.htmlTest')


// but1.click(() => console.log('but1'))

butMin.click(e => {
    console.log(e);
    //читаем координаты клика
    let x = e.clientX;
    let y = e.clientY;
    //вычисляем середину кнопки
    let box = but10min.elements[0].getBoundingClientRect();
    box.middleX = box.left + box.width/2
    box.middleY = box.top + box.height/2
    console.log({
        top: box.top + pageYOffset,
        left: box.left + pageXOffset
      });
    if (y>box.middleY) {
        but10min.text(Number(but10min.text())-1);
    }
    else{
        but10min.text(Number(but10min.text())+1);
    }
    console.log(box)
})
// but1.click(() => {
// 	but.class('btn btn-success');
// 	h1.text('btn-success')
// 	htmlTest.html('<h2>h2</h2>')
// })
// but2.click(() => {
// 	but.class('btn btn-danger');
// 	h1.text('btn-danger')
// 	htmlTest.html('<h3>h3</h3>')
// })
// but3.click(() => {
// 	but.class('btn btn-warning');
// 	h1.text('btn-warning')
// 	htmlTest.html('<h4>h4</h4>')
// })
// but4.click(() => {
// 	but.class('btn btn-primary');
// 	h1.text('btn-primary')
// 	htmlTest.html('<h5>h5</h5>')
// })
