let pbValue = 0;

function givePBValue(value) {
    $("#my-progress-bar").width(value+"%");
  }
  
function plusValue(value) {
    pbValue = pbValue + value;
    if (pbValue > 100) {
        pbValue = 100
    }
    if (pbValue < 0) {
        pbValue = 0
    }
    givePBValue(pbValue);
}

function init() {
    givePBValue(pbValue);
    $('#1pc').click(function() {
      plusValue(1);
    });
    $('#3pc').click(function() {
      plusValue(3);
    });
    $('#7pc').click(function() {
      plusValue(7);
    });
    console.log("скрипт подгрузился");
  }
  
    $(document).ready(init);