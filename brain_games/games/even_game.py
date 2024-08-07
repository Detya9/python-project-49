from random import randint


def is_even(number):
    return ('yes', 'no')[number % 2]


def even():
    random_number = randint(1, 1000)
    correct_answer = is_even(random_number)
    return random_number, correct_answer
