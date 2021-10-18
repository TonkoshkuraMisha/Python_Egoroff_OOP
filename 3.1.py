# Magic methods (d-under methods) __str__ and __repr__

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The object Lion - {self.name}"

    def __str__(self):
        return f"Lion - {self.name}"


class Person:
    def __init__(self,name, surname, gender='male'):
        if not gender  in ['male','female']:
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender='male'
        else:
            self.gender=gender
        self.name=name
        self.surname=surname
    def __str__(self):
        if self.gender=='male':
            return f"Гражданин {self.surname} {self.name}"
        else:
            return f"Гражданка {self.surname} {self.name}"

class Vector:
    def __init__(self, *args):
        s = []
        for i in args:
            if isinstance(i, int):
                s.append(str(i))
        self.values = s
    def __str__(self):
        if len(self.values) != 0:
            a = sorted(self.values)
            n = ', '.join(a)
            return (f'Вектор({n})')
        else:
            return ("Пустой вектор")
