from random import randint

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_number, second_number):
    for number in range(min(first_number, second_number), 0, -1):
        if not first_number % number and not second_number % number:
            return str(number)


def get_question():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = f'{first_number} {second_number}'
    correct_answer = get_gcd(first_number, second_number)
    return question, correct_answer
