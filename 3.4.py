# __eq__ ==
# __ne__ !=
# __lt__ <
# __le__ <=
# __gt__ >
# __ge__ >=
class Restangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @property
    def area(self):
        return  self.a * self.b
    def __eq__(self, other):
        print('__eq__')
        if isinstance(other, Restangle):
            return self.a == other.a and self.b == other.b
    def __lt__(self, other):
        print('__lt__')
        if isinstance(other, Restangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other
    def __le__(self, other):
        print('__le__')
        return  self == other or self < other
f = Restangle(3, 4)
b  = Restangle(3, 4)


class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.rating > other
        elif isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.rating < other
        elif isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return 'Невозможно выполнить сравнение'