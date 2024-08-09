from random import randint
from math import sqrt

GAME_DESCRIPTION = 'Answer "yes" if given number is prime.' \
                   ' Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    for num in range(2, round(sqrt(number)) + 1):
        if number % num == 0:
            return False
    return True


def generate_round_data():
    question = randint(1, 1000)
    correct_answer = ('no', 'yes')[is_prime(question)]
    return question, correct_answer
