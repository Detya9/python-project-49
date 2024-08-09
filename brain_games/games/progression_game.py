from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def generate_round_data():
    start = randint(1, 100)
    step = randint(1, 100)
    length = 10
    end = start + step * length
    sequence = list(map(str, range(start, end, step)))
    ind = randint(0, length - 1)
    correct_answer = sequence[ind]
    sequence[ind] = '..'
    question = ' '.join(sequence)
    return question, correct_answer
