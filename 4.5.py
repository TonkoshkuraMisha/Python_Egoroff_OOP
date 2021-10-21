# Наследование, делегирование, delegating
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Person {self.name} {self.surname}'

    def info(self):
        print('Parent class')
        print(self)

    def breathe(self):
        print('Человек дышит')


class Doctor(Person):
    def __init__(self, name, surname, age):
        # self.name = name
        # self.surname = surname
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name} {self.surname}'

    def breathe(self):
        super().breathe()
        print('Доктор дышит')


p = Person('Ivan', 'Ivanov')
d = Doctor('Petr', 'Petrov', 25)
d.breathe()  # Человек дышит/Доктор дышит
print(p.name, p.surname)  # Ivan Ivanov
print(d.name, d.surname, d.age)  # Petr Petrov 25
d.info()  # Parent class/Doctor Petr Petrov
p.info()  # Parent class/Person Ivan Ivanov
