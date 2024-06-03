import random
from brain_games.scripts.functions import func


def calc():
    specification = 'What is the result of the expression?'
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f'{number_one} {operator} {number_two}'
    correct_answer = eval(question)
    return question, correct_answer, specification


def main():
    func.get_question_and_answer(calc)


if __name__ == '__main__':
    main()
