# Property. getter-methods and setter-methods

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Balance must be a number')
        self.__balance = value

    def del_balance(self):
        print('del balance')
        del self.__balance

    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(del_balance)


class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if isinstance(value, str) and value.count('@') == 1 and '.' in value[value.find('@'):]:
            self.__email = value
        else:
            print("Ошибочная почта")

    email = property(fget=get_email, fset=set_email)
