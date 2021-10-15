# Уровни доступа к атрибутам и методам: публичные, защищённые и приватные
# атрибуты и методы. protected, private.

class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

#    def print_data(self):
#        print(self.name, self.balance, self.passport)

#    def print_protected_data(self):
#        print(self._name, self._balance, self._passport)

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob Marly', 100_000, 117118)
#account1.print_data()
#print(account1.name)
#print(account1.balance)
#print(account1.passport)

#account1.print_protected_data()
#print(account1._name)
#print(account1._balance)
#print(account1._passport)

#account1.print_private_data()
#print(account1.__name)
#print(account1.__balance)
#print(account1.__passport)

# Даже к приватным методам есть доступ.
# Сначала узнаём все методы класса.
print(dir(account1))

# Затем выбираем нужный и он показывает нам балланс клиента.
print(account1._BankAccount__name)
print(account1._BankAccount__balance)
print(account1._BankAccount__passport)
print(account1.__class__)
print(account1.print_private_data)

