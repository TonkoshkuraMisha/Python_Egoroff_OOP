class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.__password

    @staticmethod
    def proverka(value):
        with open('1mm.txt', 'r') as dict:
            for line in dict:
                if line.strip() == value:
                    return True

    @password.setter
    def password(self,value):
        if  not isinstance(value,str):
            raise TypeError('Пароль должен быть строкой')
        if User.proverka(value):
            raise ValueError('Слишком легкий пароль')
        else:
            self.__password = value