class Cat:
    breed = "pers"

    def hello(*args):
        print("Hello, World, from Kitty!", args)

    def show_breed(instance):
        print(f'My breed is {instance.breed}')

class Lion:
    def foar(self):
        print(f'Rrrrrrr!!!')


class Counter:
    def  start_from(instance,count=0):
        instance.count = count

    def increment(instance):
        instance.count+=1

    def display(instance):
        print( f"Текущее значение счетчика = {instance.count}")

    def reset(instance):
        instance.count = 0


import math


class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, arg):
        if isinstance(arg, Point):
            return ((self.x - arg.x) ** 2 + (self.y - arg.y) ** 2) ** 0.5
        else:
            print(f'Передана не точка')
