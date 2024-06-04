import random
from brain_games.scripts.functions import func


def max_divisor(number_one, number_two):
    while number_one != 0 and number_two != 0:
        if number_one > number_two:
            number_one = number_one % number_two
        else:
            number_two = number_two % number_one
    return number_one + number_two


def gcd():
    specification = 'Find the greatest common divisor of given numbers.'
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    correct_answer = max_divisor(number_one, number_two)
    question = f'{number_one} {number_two}'
    return question, correct_answer, specification


def main():
    func.get_question_and_answer(gcd)


if __name__ == '__main__':
    main()
