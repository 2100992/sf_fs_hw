#Создаем класс-секундомер.
#Возможно как декорерования функций, так и работа в качестве контекстного менеджера.

from time import time

class time_this:

    def __init__(self, num_runs = 1):
#        print(f'Создали экземпляр time_this с параметрами {num_runs}')
        self.num_runs = num_runs
        self.time_of_completion = 0

    def __call__(self, func):
#        print(f'Вызвали экземпляр time_this как функцию с параметрами {func}')
        self.func = func
        def wrap(*args, **kwargs):
#            print(f'Вызвали функцию обертку с параметрами {args}')
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time()
                result = self.func(*args, **kwargs)
                t1 = time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs
            print("Выполнение функции %s(%s) заняло %.2f секунд" % (self.func.__name__, *args, avg_time))
            return result
        return wrap

    #засекаем время входа в контекст
    def __enter__(self):
        self.t0 = time()
        return self

    #После выполнения всего кода вычитаем из времени выхода время входа.
    #Результат на печать
    def __exit__(self, *args, **kwargs):
        self.t1 = time()
        self.time_of_completion = (self.t1 - self.t0)
        print("Выполнение функции заняло %.2f секунд" % self.time_of_completion)


#Тест декорирования функции f1
@time_this(num_runs = 10)
def f1(iterations):
    for _ in range(iterations):
        pass
    return f"Закончили {iterations} пустых циклов"

print('Вывод результата исполнения декорированной функции')
print(f1(10000000), '\n')




#Тест контеткстного менеджера на функции f2
def f2(iterations):
    for _ in range(iterations):
        pass
    return f"Закончили {iterations} пустых циклов"

print('Вывод результата исполнения функции внутри контекстного менеджера')
with time_this():
    print(f2(10000000))