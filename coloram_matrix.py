import colorama
import random
from colorama import Fore, Back, Style

colorama.init()
print(Fore.LIGHTGREEN_EX + 'green')
from termcolor import colored, cprint
print(colored('Привет мир!', 'red', attrs=['underline']))
print('Привет, я люблю тебя!')
cprint('Вывод с помощью cprint', 'green', 'on_blue')
# print(Back.BLUE + 'Синий фон')
# print(Style.RESET_ALL)
# print('Снова обычный текст')