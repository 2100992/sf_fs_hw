class time_this:
    def __init__(self, num_runs):
        print(f'Создали экземпляр time_this с параметрами {num_runs}')
        self.num_runs = num_runs

    def __call__(self, func):
        print(f'Вызвали экземпляр time_this как функцию с параметрами {func}')
        self.func = func
        def wrap(*args):
            print(f'Вызвали функцию обертку с параметрами {args}')
            from time import time
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time()
                result = self.func(*args)
                t1 = time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs
            print("Выполнение функции %s(%s) заняло %.2f секунд" % (self.func.__name__, *args, avg_time))
            return result
        return wrap

@time_this(num_runs = 10)
def f(iterations):
    for _ in range(iterations):
        pass
    return f"Закончили {iterations} пустых циклов"

print(f(10000000))