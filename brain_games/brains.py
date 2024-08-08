from brain_games.greetings import welcome_user


def brains(game, attempts=3):
    username = welcome_user()
    print(game.GAME_DESCRIPTION)
    for i in range(attempts):
        question, correct_answer = game.get_question()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer"
                  f" ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return
        print('Correct!')
    print(f'Congratulations, {username}!')
