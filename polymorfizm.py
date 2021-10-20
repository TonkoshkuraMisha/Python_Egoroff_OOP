
class Restangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'Restangle {self.a} x {self.b} = {self.a * self.b}'
    #def get_rect_area(self):# был ранее
    def get_area(self):
        return  self.a * self.b
class Square:
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f'Square {self.a} ** 2 = {self.a ** 2}'
    #def get_sq_area(self):# был ранее
    def get_area(self):
        return  self.a ** 2
class Cirkle:
    def __init__(self, r):
        self.r = r
    def __str__(self):
        return f'Cirkle r = {3.14 * self.r ** 2}'
    #def get_cir_area(self):# был ранее
    def get_area(self):
        return  3.14 * self.r ** 2

