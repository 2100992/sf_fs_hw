const numDivs = 36;
const maxHits = 10; //количество попаданий для окончания игры

let horisontalDivs = 6; //размер игрового поля по горизонтали
let verticalDivs = 6; //размер игрового поля по вертикали

let hits = 0;
let firstHitTime = 0;


// FIXME: как вставлять в JS переменную в строку?
const gameFieldDiv1 = '<div class="grid-item game-field" id="slot-'
const gameFieldDiv2 = '"></div>'


//Формируем игровое поле заданной размерности
function buildGameField(x, y) {
  for(let i = 1; i <= x; i++) {
    for(let j = 1; j <= y; j++) {
      $('.gameField').append(gameFieldDiv1 + i + j + gameFieldDiv2);
    }
  }
  $('.grid-wrapper').css('grid-template-columns', 'repeat(' + x + ', 1fr)');
  $('.grid-wrapper').css('grid-template-rows', 'repeat(' + y + ', 1fr)');
  $('.grid-wrapper').css('grid-gap', (3/x)+'vw');
}


function round() {
  let divSelector = randomDivId(horisontalDivs, verticalDivs);
  $(divSelector).addClass("target");
  $(divSelector).html(hits); // помечаем target текущим номером
  firstHitTime = getTimestamp()
  // FIXME: тут надо определять при первом клике firstHitTime

  if (hits === maxHits) {
    endGame();
  }
}

function endGame() {
  // FIXME: спрятать игровое поле сначала

  let totalPlayedMillis = getTimestamp() - firstHitTime;
  let totalPlayedSeconds = Number(totalPlayedMillis / 1000).toPrecision(3);
  $("#total-time-played").text(totalPlayedSeconds);
  $("#win-message").removeClass("d-none");
}

function handleClick(event) {
  // FIXME: убирать текст со старых таргетов. Кажется есть .text?
  if ($(event.target).hasClass("target")) {
    $(event.target).removeClass("target");
    $(event.target).html("");
    hits = hits + 1;
    round();
  }
  else {
    $(event.target).hasClass("miss");
  }
  
  // TODO: как-то отмечать если мы промахнулись? См CSS класс .miss
}

function init() {
  // TODO: заказчик просил отдельную кнопку, запускающую игру а не просто по загрузке
  buildGameField(horisontalDivs, verticalDivs)
  round();

  $(".game-field").click(handleClick);

  $("#button-reload").click(function() {
    location.reload();
  });
}

$(document).ready(init);
