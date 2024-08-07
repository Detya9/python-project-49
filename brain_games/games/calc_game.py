from random import randint, choice


def calc():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    number_for_multi = randint(1, 10)
    operation = choice(['-', '+', '*'])
    if operation == '*':
        question = f'{first_number} {operation} {number_for_multi}'
    else:
        question = f'{first_number} {operation} {second_number}'
    correct_answer = str(eval(question))
    return question, correct_answer
