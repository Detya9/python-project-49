from random import randint
from math import sqrt


def prime():
    question = randint(1, 1000)
    correct_answer = 'yes'
    if question == 1:
        correct_answer = 'no'
    for number in range(2, round(sqrt(question)) + 1):
        if question % number == 0:
            correct_answer = 'no'
            break
    return question, correct_answer
