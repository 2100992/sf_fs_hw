def fib(n):
    a, b = 1, 1  # задаем начальные значения
    for x in range(n):  # в цикле for повторяем n раз подсчет очередного элемента
        yield a  # с помощью ключевого слова yield возвращаем текущий элемент а
        a, b = b, a + b  # подсчитываем следующее значение

a = []
for i in fib(20):
    a.append(i)

print(a)


fibonacci_sequence = fib(20)

print(next(fibonacci_sequence))
print(next(fibonacci_sequence))
print(next(fibonacci_sequence))
print(next(fibonacci_sequence))
print(next(fibonacci_sequence))
print(next(fibonacci_sequence))
print(next(fibonacci_sequence))
print(next(fibonacci_sequence))
print(next(fibonacci_sequence))


for item in list(fib(20)):
    print(item)


f = fib(20)
print(f)
print(list(f))