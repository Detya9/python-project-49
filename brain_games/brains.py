import prompt


def start(game, attempts=3):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.GAME_DESCRIPTION)
    for i in range(attempts):
        question, correct_answer = game.generate_round_data()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer"
                  f" ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {username}!')
