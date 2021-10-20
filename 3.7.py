# magic methods
# method __call__

class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Method __call__ was called {self.counter} times')

    def average(self):
        return self.summa / self.length


from time import perf_counter


class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        return result

@Timer
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr

@Timer
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)
