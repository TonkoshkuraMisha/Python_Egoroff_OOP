# magic method __bool__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__ called')
        return abs(self.x - self.y)

    def __bool__(self):
        print('__bool__')
        return self.x != 0 or self.y != 0

class City:
    def __init__(self, city):
        self.name = city.title()
    def __str__(self):
        return self.name
    def __bool__(self):
        if self.name[-1] in "aeiou":
            return False
        return True


class Quadrilateral:
    def __init__(self,*args):
        self.width=args[0]
        self.height=args[-1]
    def __str__(self):
        if self.width==self.height:
            return f"Куб размером {self.width}х{self.height}"
        else:
            return f"Прямоугольник размером {self.width}х{self.height}"
    def __bool__(self):
        return self.width==self.height