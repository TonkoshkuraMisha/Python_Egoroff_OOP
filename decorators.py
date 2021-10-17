# Декораторы. Примеры.
from functools import wraps

def header(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


@header
@table
def say(name, lastname):
    print(f"Hello, {lastname} {name}!")


say('Tonkoshkura', 'Misha')


def sqr(x):
    """
    Возведение в квадрат аргумента.
    :param x:
    :return:
    """
    print(x**2)