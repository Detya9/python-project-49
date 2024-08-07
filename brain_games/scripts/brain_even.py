#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint


def is_even(number):
    return ('yes', 'no')[number % 2]


def main():
    username = welcome_user()
    attempts = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(attempts):
        random_number = randint(1, 1000)
        correct_answer = is_even(random_number)
        print(f'Question: {random_number}')
        answer = input('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return
        print('Correct!')
    print(f'Congratulations, {username}!')


if __name__ == '__main__':
    main()
