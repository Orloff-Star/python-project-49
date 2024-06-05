import random


SPECIFICATION = 'Find the greatest common divisor of given numbers.'


def is_max_divisor(number_one, number_two):
    while number_one != 0 and number_two != 0:
        if number_one > number_two:
            number_one = number_one % number_two
        else:
            number_two = number_two % number_one
    return number_one + number_two


def user_interaction():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    correct_answer = is_max_divisor(number_one, number_two)
    question = f'{number_one} {number_two}'
    return question, correct_answer
