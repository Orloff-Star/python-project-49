import random


SPECIFICATION = 'What is the result of the expression?'


def user_interaction():
    
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
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
