from brain_games.cli import welcome_user


def brains(function, attempts=3):
    username = welcome_user()
    print(games_description.get(function.__name__))
    for i in range(attempts):
        question, correct_answer = function()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer"
                  f" ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return
        print('Correct!')
    print(f'Congratulations, {username}!')


games_description = {
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
}
