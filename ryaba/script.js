const ryabaLink = 'https://api.myjson.com/bins/jcmhn';
const aboutText = 'Домашнее задание по модулю 5';
let story = '';

function getRyabaStory(link) {
    $.getJSON(link, function() {
        console.log("success");
    })
        .done(function(data) {
            console.log('success get');
            console.log(data);
            story = data;
            return story;
        })
        .fail(function() {
            console.log('error get');
            return 'ошибка получения JSON'
        });
};

function getStory(link) {
    $.getJSON(link)
    .done(function(answer) {
        console.log(answer)
    }
    )
}

let ryabaStory = getRyabaStory(ryabaLink);

function returnAbout(text) {
    console.log(text)
    const $result = $('.result');
    $result.html(text);
};


$(document).ready(function() {
    console.log('');

    $("#about").click(function() {
        returnAbout(aboutText);
    });
    
    $(".btn").click(function() {
        getRyabaStory(ryabaLink);
    });
    
    }
);


/*
$('.btn').click(testReturn());
*/

