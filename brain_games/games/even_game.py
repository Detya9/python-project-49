from random import randint

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return ('yes', 'no')[number % 2]


def get_question():
    random_number = randint(1, 1000)
    correct_answer = is_even(random_number)
    return random_number, correct_answer
