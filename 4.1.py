# Наследование

class Person: # parent class

    def can_breathe(self):
        print('I can breathe')

    def can_walk(self):
        print('I can walk')


class Doctor(Person): # subclass

    def can_cure(self):
        print('I can cure')


class Architect(Person): # subclass

    def can_build(self):
        print('I can build')


class Optometrist(Doctor):

    def can_treat_eyesight(self):
        print('I can treat eyesight')



# We can:
d = Doctor()
a = Architect()
o = Optometrist()
print('Doctor:')
d.can_walk()
d.can_breathe()
d.can_cure()
print('Architect:')
a.can_walk()
a.can_breathe()
a.can_build()
print('Optometrist:')
o.can_walk()
o.can_breathe()
o.can_cure()
o.can_treat_eyesight()

# But we can`t:
# d.can_build()
# a.can_cure()
print()
print(issubclass(Doctor, Person))
print(issubclass(Architect, Doctor))
print(issubclass(Optometrist, Doctor))
print(issubclass(Optometrist, Person))
print()
print(isinstance(d, Doctor))
print(isinstance(a, Architect))
print(isinstance(d, Person))
print(isinstance(a, Person))
print()
print(isinstance(a, Doctor))
print(isinstance(d, Architect))
print()
print(isinstance(o, Optometrist))
print(isinstance(o, Doctor))
print(isinstance(o, Person))
print(isinstance(o, Architect))