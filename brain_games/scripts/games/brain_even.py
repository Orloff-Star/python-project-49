import random
from brain_games.scripts.functions import func


def even():
    specification = 'Answer "yes" if the number is even, otherwise answer "no".'
    random_number = random.randrange(0, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'{random_number}'
    return question, correct_answer, specification


def main():
    func.get_question_and_answer(even)


if __name__ == '__main__':
    main()
