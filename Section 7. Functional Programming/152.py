from time import time


def perfomance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'too {t2 - t1} s')
        return result
    return wrapper


@perfomance
def long_time():
    for i in range(10000000):
        i * 5


long_time()
