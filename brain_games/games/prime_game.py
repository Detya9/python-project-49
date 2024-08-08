from random import randint
from math import sqrt

GAME_DESCRIPTION = 'Answer "yes" if given number is prime.' \
                   'Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return 'no'
    for num in range(2, round(sqrt(number)) + 1):
        if number % num == 0:
            return 'no'
    return 'yes'


def get_question():
    question = randint(1, 1000)
    correct_answer = is_prime(question)
    return question, correct_answer
