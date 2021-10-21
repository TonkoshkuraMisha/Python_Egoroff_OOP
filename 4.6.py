class Base:
    __slots__ = ('a', 'b')

    def __init__(self, a: int, b: int) -> None:
        print('Инициализация: класс Base')
        self.a = a
        self.b = b

    def sub_method(self, b):
        # Метод базового класса Base
        print('Вызов sub_method базового класса Base:', b)


class FirstLvl(Base):
    __slots__ = tuple()

    def __init__(self, a: int, b: int) -> None:
        print('Инициализация: класс FirstLvl')
        super().__init__(a=a, b=b)

    def sub_method(self, b):
        print('Вызов sub_method класса FirstLvl:', b)
        # Делегирование запроса методу класса Base
        super().sub_method(b + 1)


class SecondLvl(FirstLvl):
    __slots__ = tuple('c')

    def __init__(self, a: int, b: int, c: int) -> None:
        # Добавили атридут 'c'
        print('Инициализация: класс SecondLvl')
        super().__init__(a=a, b=b)
        self.c = c

    def sub_method(self, b):
        print('Вызов sub_method класса SecondLvl:', b)
        # Делегирование запроса методу класса FirstLvl
        super().sub_method(b + 1)


class ThirdLvl(SecondLvl):
    __slots__ = tuple()

    def __init__(self, a: int, b: int) -> None:
        print('Инициализация: ThirdLvl class')
        # super() начнёт поиск на уровень выше класса SecondLvl.
        # Следовательно атрибут 'c' класса SecondLvl не учитывается при инициализации
        super(SecondLvl, self).__init__(a=a, b=b)

    def sub_method(self, b):
        print('Вызов sub_method класса ThirdLvl:', b)
        # super() начнёт поиск на уровень выше класса SecondLvl.
        # Вызов метода будет делегирован на уровень выше класса SecondLvl классу FirstLvl
        super(SecondLvl, self).sub_method(b + 1)


b = Base(2, 3)
b.sub_method(2)

first = FirstLvl(3, 4)
first.sub_method(2)

second = SecondLvl(2, 3, 4)
second.sub_method(2)

third = ThirdLvl(4, 5)
third.sub_method(2)
