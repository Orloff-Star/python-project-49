import random


SPECIFICATION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_OF_RANGE = 1
END_OF_RANGE = 300


def is_prime_num(num):
    if num <= 1:
        return False
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


def calculate_answer():
    random_number = random.randrange(START_OF_RANGE, END_OF_RANGE)
    answer = is_prime_num(random_number)
    if answer is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'{random_number}'
    return question, correct_answer
