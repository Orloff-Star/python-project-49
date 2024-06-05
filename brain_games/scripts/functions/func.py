import prompt


ATTEMPT = 3


def get_question_and_answer(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.SPECIFICATION)
    i = 0
    while i < ATTEMPT:
        question, correct_answer = game.user_interaction()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ').lower()

        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
        i = i + 1

    print(f'Congratulations, {name}!')
