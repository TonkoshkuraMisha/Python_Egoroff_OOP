class Cat:
    breed = "pers"

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def __init__(self, name, breed='pers', age=1, color='white'):
        print('Hello', self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'


laptop1 = Laptop('macbook air', '13-inch', 99000)
laptop2 = Laptop('macbook pro', '15-inch', 195000)


class SoccerPlayer:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, value=1):
        self.goals += value

    def make_assist(self, value=1):
        self.assists += value

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

class Zebra:
    def __init__(self):
        self.count = 1
    def which_stripe(self):
        if self.count %2 == 1:
            print('Полоска белая')
            self.count +=1
        else:
            print('Полоска черная')
            self.count += 1