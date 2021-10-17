# Пример замыкания. Аналогичные действия могут производить экземпляры классов в ООП.
def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


def average_numbers():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa, count
        summa += number
        count += 1
        return summa / count

    return inner


from datetime import datetime
from time import perf_counter


def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner


def add(a, b):
    return a + b

def count_func(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция {func.__name__}() вызывалась {count} раз.")
        return func(*args, **kwargs)

    return inner
