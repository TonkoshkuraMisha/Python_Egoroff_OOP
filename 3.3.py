# __addf__(+), __mul__(*),__sub__(-), __truediv__(/)

class BancAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BancAccount):  # проверяем явл ли экземпляром этого (BancAccount) класса
            return self.balance + other.balance  # слож баланса другого экз этого (BancAccount) класса
        if isinstance(other, (int, float)):  # проверяем явл ли числом
            return self.balance + other
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ call')
        return self + other

    def __mul__(self, other):
        print('__mul__ call')
        if isinstance(other, BancAccount):  # проверяем явл ли экземпляром этого (BancAccount) класса
            return self.balance * other.balance  # умнож баланса другого экз этого (BancAccount) класса
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):  # проверяем явл ли строкой
            return self.name + other
        # raise NotImplemented

    def __rmul__(self, other):
        print('__rmul__ call')
        return self * other


r = BancAccount('Ivan', 900)  # __add__ call
print(r + 600, r.balance + 300, r.balance)  # 1500 1200 900
b = BancAccount('Luka', 1900)  # __add__ call
print(r + b, b + 600, b.balance + 300, b.balance)  # 2800 2500 2200 1900
print(600 + r)  # 1500


# __addf__(+), __mul__(*),__sub__(-), __truediv__(/)

class BancAccount:
    def __init__(self, name, balance):
        print('New object __init__')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BancAccount):  # проверяем явл ли экземпляром этого (BancAccount) класса
            return self.balance + other.balance  # слож баланса другого экз этого (BancAccount) класса
        if isinstance(other, (int, float)):  # проверяем явл ли числом
            # return self.balance + other
            return BancAccount(self.name, self.balance + other)  # Возвращаем новый экземпляр
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ call')
        return self + other


t = BancAccount('Vasja', 900)  # New object __init__
print(id(t))  # 140062794291240
print(t + 30)  # Клиент Vasja с балансом 930

# task - Vectors add and multiply
class Vector:
    def __init__(self, *args):
        self.values = []
        for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)
        self.values.sort()

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(self.values)}'
        return 'Пустой вектор'

    def __add__(self, other):
        new_v = []
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] + other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('Сложение векторов разной длины недопустимо')
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] + other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        new_v = []
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] * other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('Умножение векторов разной длины недопустимо')
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] * other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя умножать с {other}')
