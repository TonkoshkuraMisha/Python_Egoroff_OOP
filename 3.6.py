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
