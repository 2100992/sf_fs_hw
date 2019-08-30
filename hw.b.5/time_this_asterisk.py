class time_this:
    def __init__(self, num_runs):
        self.num_runs = num_runs
        print('__init__ прошел')
        print(f'num_runs = {self.num_runs}')

    def __call__(self):
        from time import time
        def decorator(func):
            def wrap(*args, **kwargs):
                avg_time = 0
                for _ in range(self.num_runs):
                    t0 = time()
                    result = func(*args, **kwargs)
                    t1 = time()
                    avg_time += (t1 - t0)
                avg_time /= num_runs
                print("Выполнение функции %s%s заняло %.2f секунд" % (func.__name__, args, avg_time))
                return result
            return wrap
        return decorator

'''
@time_this(num_runs = 10)
def f1():
    for _ in range(2000000):
        pass
    return "Закончили процедуры"
'''

#@time_this(num_runs = 10)
def f2(iterations):
    for _ in range(iterations):
        pass
    return "Закончили процедуры"

deco = time_this(10)
f2 = deco(f2)

#f1()
f2(10000000)