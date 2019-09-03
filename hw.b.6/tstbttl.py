from bottle import route
from bottle import run
from bottle import request
from bottle import HTTPError

@route('/hello/')
def hello_world():
    return 'Hello World!'

@route("/upper/<param>")
def upper(param):
    return param.upper()

@route("/modify/<param>/<method>")
def modify(param, method):
    # проверяем переданный модификатор и готовим соответствующий результат
    if method == "upper":
        result = param.upper()
    elif method == "lower":
        result = param.lower()
    elif method == "title":
        result = param.title()
    else:
       	# если нам передан неизвестный модификатор, готовим ответ для пользователя 
        result = HTTPError(400, "incorrect `method` value")
    return result

def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a

@route("/fib/<n:int>")
def fib_handler(n):
    result = fib(n)
    return str(result)

@route("/add")
def add():
    #получаем значения GET-параметров x и y
    try:
        x = int(request.query.x)
        y = int(request.query.y)
    except ValueError:
        result = HTTPError(400, "Некорректные параметры")
    else:
        s = x + y
        result = "Сумма {} и {} равна {}".format(x, y, s)
    return result

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
