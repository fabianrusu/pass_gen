import random
import string

char_list = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)


def pass_gen(number):
    pass_list = random.choices(char_list, k=number)
    password = ''.join(pass_list)
    return password


def user_input():
    print('>>>>>>>>>>Hello!<<<<<<<<<<\nWelcome to Password Generator')
    length = input('Enter the length of your password: ')
    while int(length) < 8:
        print('Minimum password length is 8 characters.')
        length = input('Enter the length of your password: ')
    return int(length)


user_pass = pass_gen(user_input())
print(user_pass)
