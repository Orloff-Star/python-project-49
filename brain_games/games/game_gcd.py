import random
import math


SPECIFICATION = 'Find the greatest common divisor of given numbers.'
START_OF_RANGE = 1
END_OF_RANGE = 100


def ask_question_get_answer():
    number_one = random.randint(START_OF_RANGE, END_OF_RANGE)
    number_two = random.randint(START_OF_RANGE, END_OF_RANGE)
    correct_answer = math.gcd(number_one, number_two)
    question = f'{number_one} {number_two}'
    return question, correct_answer
