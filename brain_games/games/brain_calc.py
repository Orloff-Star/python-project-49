import random


SPECIFICATION = 'What is the result of the expression?'
START_OF_RANGE = 1
END_OF_RANGE = 100


def calculate_answer():
    number_one = random.randint(START_OF_RANGE, END_OF_RANGE)
    number_two = random.randint(START_OF_RANGE, END_OF_RANGE)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f'{number_one} {operator} {number_two}'
    if operator == '+':
        correct_answer = number_one + number_two
    elif operator == '-':
        correct_answer = number_one - number_two
    elif operator == '*':
        correct_answer = number_one * number_two
    return question, correct_answer
