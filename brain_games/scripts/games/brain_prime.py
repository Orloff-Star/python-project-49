import random


SPECIFICATION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_num(num):
    if num <= 1:
        return False
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


def user_interaction():
    random_number = random.randrange(0, 300)
    ans_wer = is_prime_num(random_number)
    if ans_wer is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'{random_number}'
    return question, correct_answer
