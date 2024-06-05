import random


SPECIFICATION = 'Answer "yes" if the number is even, otherwise answer "no".'


def user_interaction():
    random_number = random.randrange(0, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'{random_number}'
    return question, correct_answer
