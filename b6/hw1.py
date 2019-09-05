import math

from bottle import route
from bottle import run
from bottle import HTTPError


@route('/add/<x:int>/<y:int>')
def add(x, y):
    result = x + y
    return str(result)

@route('/subtract/<x:int>/<y:int>')
def subtract(x, y):
    result = x - y
    return str(result)

@route('/multiply/<x:int>/<y:int>')
def multiply(x, y):
    result = x * y
    return str(result)

@route('/div/<x:int>/<y:int>')
def div(x, y):
    if y == 0:
        result = HTTPError(400, "zero_division")
    else:
        result = str(x / y)
    return result

@route('/sqrt/<x:int>/')
def sqrt(x):
    result = math.sqrt(x)
    return str(result)

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)