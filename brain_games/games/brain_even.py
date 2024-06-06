import random


SPECIFICATION = 'Answer "yes" if the number is even, otherwise answer "no".'
START_OF_RANGE = 1
END_OF_RANGE = 100


def calculate_answer():
    random_number = random.randrange(START_OF_RANGE, END_OF_RANGE)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'{random_number}'
    return question, correct_answer
