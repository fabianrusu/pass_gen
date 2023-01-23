import random

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '!', '?']
# number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# char_list = ['.', '!', '?']


def pass_gen(number):
    count = 0
    password = ''
    while count < number:
        letter = random.choice(letter_list)
        password += letter
        count = count + 1

    return password


def user_input():
    print('>>>>>>>>>>Hello!<<<<<<<<<<\nWelcome to Password Generator v1.1')
    length = input('Enter the length of your password: ')
    while int(length) < 6:
        print('Minimum password length is 6 characters.')
        length = input('Enter the length of your password: ')
    return int(length)


user_pass = pass_gen(user_input())
print(user_pass)
