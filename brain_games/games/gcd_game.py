from random import randint


def gcd():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = f'{first_number} {second_number}'
    for number in range(min(first_number, second_number), 0, -1):
        if not first_number % number and not second_number % number:
            correct_answer = str(number)
            break
    return question, correct_answer
