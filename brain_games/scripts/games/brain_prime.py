import random
from brain_games.scripts.functions import func


def prime_num(num):
    if num <= 1:
        return False
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


def prime():
    specific = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    random_number = random.randrange(0, 300)
    ans_wer = prime_num(random_number)
    if ans_wer is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'{random_number}'
    return question, correct_answer, specific


def main():
    func.get_question_and_answer(prime)


if __name__ == '__main__':
    main()
