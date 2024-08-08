from random import randint, choice

GAME_DESCRIPTION = 'What is the result of the expression?'


def get_answer(first_number, second_number, operator):
    match operator:
        case '*':
            return int(first_number) * int(second_number)
        case '-':
            return int(first_number) - int(second_number)
        case '+':
            return int(first_number) + int(second_number)


def get_question():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    number_for_multi = randint(1, 10)
    operation = choice(['-', '+', '*'])
    if operation == '*':
        second_number = number_for_multi
    question = f'{first_number} {operation} {second_number}'
    correct_answer = str(get_answer(first_number, second_number, operation))
    return question, correct_answer
