# Полиморфизм
from polymorfizm import Restangle, Square, Cirkle

a = Restangle(2, 4)
b = Restangle(4, 9)
#print(a.get_rect_area(), b.get_rect_area())# 8 36
print(a.get_area(), b.get_area())# 8 36
c1 = Square(5)
c2 = Square(8)
#print(c1.get_sq_area(), c2.get_sq_area())# 25 64
print(c1.get_area(), c2.get_area())# 25 64
cir1 = Cirkle(9)
cir2 = Cirkle(4)
#print(cir1.get_cir_area(), cir2.get_cir_area())# 254.34 50.24
print(cir1.get_area(), cir2.get_area())# 254.34 50.24
figures = [a, b, c1, c2, cir1, cir2]
for figure in figures:
    #if isinstance(figure, Square):
    #    print(figure.get_sq_area())
    #elif isinstance(figure, Cirkle):
    #    print(figure.get_cir_area())
    #else:
    #    print(figure.get_rect_area())
    print(figure.get_area())
print(a)
print(b)
print(c1)
print(c2)
print(cir1)
print(cir2)