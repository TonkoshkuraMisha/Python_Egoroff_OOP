# classmethod and staticmethod

class Example:
    def hello(self):
        print('Hello!')

    def instance_hello(self):
        print(f'instance_hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')

    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')

class Robot:
    population = 0
    def __init__(self , name):
        self.name = name
        Robot.population += 1
        print(f"Робот {self.name} был создан")
    def destroy(self):
        print(f"Робот {self.name} был уничтожен")
        Robot.population -= 1
    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")
    @classmethod
    def how_many(cls):
        print(f"{cls.population}, вот сколько нас еще осталось")