import random
from brain_games.scripts.functions import func


def max_divisor(number_one, number_two):
    list_of_divisors = []
    if number_one >= number_two:
        i = 1
        while i <= number_two:
            if number_one % i == 0 and number_two % i == 0:
                list_of_divisors.append(i)
                i += 1
            else:
                i += 1
    elif number_one < number_two:
        i = 1
        while i <= number_one:
            if number_one % i == 0 and number_two % i == 0:
                list_of_divisors.append(i)
                i += 1
            else:
                i += 1
    return (list_of_divisors)


def gcd():
    specification = 'Find the greatest common divisor of given numbers.'
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    list_div = max_divisor(number_one, number_two)
    correct_answer = max(list_div)
    question = f'{number_one}  {number_two}'
    return question, correct_answer, specification


def main():
    func.get_question_and_answer(gcd)


if __name__ == '__main__':
    main()
