const ryabaLink = 'https://api.myjson.com/bins/jcmhn';
const aboutText = 'Домашнее задание по модулю 5';
let story = '';
let res = '';
const $result = $('.result');
const $spinner = $('.spinner-border');
let count = 0;

const varr = [
    'var1',
    'var2',
    'var3',
    'var4',
    'var5',
    'var6',
    'speach'
]

function getRyabaJSON(link) {  // Получаем заготовку сценария
    $.getJSON(link, function() {
        console.log("success");
    })
        .done(function(data) {
            console.log('success get');
            console.log(data);
            story = data['text'];
            story = var2span(getRyabaStory(story), varr);
            $result.html(story);
            readVal(varr);
            despin();
        })
        .fail(function() {
            console.log('error get');
            story = 'ERROR getting JSON!!!';
            $result.html(story);
            despin();
        });
};



function getRyabaStory(arr) {
    let text = '';
    for(let i = 0; i < arr.length; i++) {
        text = text + '<p>' + arr[i] + '</p>';
    };
    return text;
}

function var2span(text, arr) {
    let oldStr = '';
    let newStr = '';
    for(let i = 0; i < arr.length; i++) {
        oldStr = new RegExp('{' + arr[i] + '}', 'g');
        newStr = '<span class = "' + arr[i] + '">' + arr[i] + '</span>'
        text = text.replace(oldStr, newStr);
    };
    return text;
};


function readVal(arr) {
    for(let i = 0; i < arr.length; i++) {
        $('.' + arr[i]).html($('#'+arr[i]).val());
    };
};

function despin() {
    $spinner.css("display", "none");
};

function spin() {
    $spinner.css("display", "inline-block");
};

function testTimeout() {
    spin();
    setTimeout(function() {despin()}, 2000);
}

function redFlash(jqObj) {
    for(let i = 255; i > 0; i--) {
        jqObj.css('background-color', 'rgb(255, ' + i +', ' + i +')');
    };
}

function returnAbout(text) {
    console.log(text)
    const $result = $('.result');
    $result.html(text);
};




$(document).ready(function() {
    console.log('document ready');

    $("#about").click(function() {
        returnAbout(aboutText);
    });
    
    $(".btn").click(function() {
        console.log('button clicked');
        spin();
        getRyabaJSON(ryabaLink);

    });
    
    }
);