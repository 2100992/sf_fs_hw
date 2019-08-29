def time_this(num_runs):
    from time import time
    def decorator(func):
        def wrap(*args, **kwargs):
            avg_time = 0
            for _ in range(num_runs):
                t0 = time()

                func(*args, **kwargs)
                
                t1 = time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение функции %s%s заняло %.2f секунд" % (func.__name__, args, avg_time))
            return "Выполнение функции %s%s заняло %.2f секунд" % (func.__name__, args, avg_time)
        return wrap
    return decorator


@time_this(num_runs = 10)
def f1():
    for _ in range(2000000):
        pass

@time_this(num_runs = 10)
def f2(iterations):
    for _ in range(iterations):
        pass


f1()

f2(10000000)