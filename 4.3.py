class Person:

    def __init__(self, name):
        print('init Person')
        self.name = name

    def breathe(self):
        print('Person breathe')

    def walk(self):
        print('Person walk')

    def sleep(self):
        print('Person sleep')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):
        return f"Person {self.name}"


class Doctor(Person):

    def breathe(self):
        print('Doctor breathe')

    def walk(self):
        print('Doctor walk')

    def sleep(self):
        print('Doctor sleep')

    def __str__(self):
        return f"Doctor {self.name}"

p = Person('Adam')
d = Doctor('John')
p.combo()
d.combo()
