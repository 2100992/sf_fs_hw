NUM_RUNS = 1000000

def time_this(num_runs):
    from time import time
    def decorator(func):
        def wrap(*args, **kwargs):
            avg_time = 0
            for _ in range(num_runs):
                t0 = time()
                result = func(*args, **kwargs)
                t1 = time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение функции %s%s заняло %.2f секунд" % (func.__name__, args, avg_time))
            return result
        return wrap
    return decorator

@time_this(num_runs = 10)
def f1():
    for _ in range(2000000):
        pass
    return f"Закончили 2000000 пустых циклов"

@time_this(num_runs = 10)
def f2(iterations):
    for _ in range(iterations):
        pass
    return f"Закончили {iterations} пустых циклов"

def f3(iterations):
    for _ in range(iterations):
        pass
    return f"Закончили {iterations} пустых циклов"
'''
deco = time_this(10)
f3 = deco(f3)
'''

def main():
    print(f1())
    print(f2(2000000))
    print(f3(1000000))

if __name__ == "__main__":
    deco = time_this(10)
    f3 = deco(f3)
    main()



'''

new_decorator = time_this(num_runs = NUM_RUNS)

f4 = new_decorator(f3)

f4(100000)

f = time_this()

'''

#f(10000000) это эквивалент time_this(num_run = 10)(f)(1000000)


