let ryabaString = 'Жили-были {var1} да {var2} Была у них {var3} Снесла {var3} {var4}, не простое - золотое - {var1} бил, бил - не разбил - {var2} била, била - не разбила {var5} бежала, {var6} задела, {var4} упало и разбилось. {var1} плачет, {var2} плачет, а {var3} кудахчет: {speach}'


$(document).ready(function() {
    $.('.btn').click(function() {
        const $result = $('.result');
        $result.hml(ryabaString);
    })
    }
)

