class Point:
    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f"Point with coordinates: ({self.x}, {self.y})")

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен быть точка!')
        else:
            return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        self.sound = sound
        return f"{self.name} says {self.sound}"


class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        if self.values:
            return False
        else:
            return True

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.is_empty() is False:
            return self.values.pop()
        else:
            print("Empty Stack")

    def peek(self):
        if self.is_empty()  is False:
            return self.values[-1]
        else:
            print("Empty Stack")
            return None

    def size(self):
        return len(self.values)