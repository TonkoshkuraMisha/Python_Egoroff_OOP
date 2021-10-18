class Person:
    name = "Ivan"
    age = 30

print(Person)
print(Person.age)
print(Person.name)

print(Person.__dict__)

print(getattr(Person, 'age'))
setattr(Person, 'lastname', "Ivanov")
print(Person.lastname)