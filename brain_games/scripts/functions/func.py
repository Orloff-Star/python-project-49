import random


def greeting():
    print("Welcome to the Brain Games!")
    print('May I have your name? ', end='')


if __name__ == "__main__":
    greeting()


incorrect_unswer = "is wrong answer ;(. Correct answer was"


def random_number():
    return random.randint(0, 100)


if __name__ == "__main__":
    random_number()


operators = ['+', '-', '*']


def choose_operator():
    return random.choice(operators)


if __name__ == "__main__":
    choose_operator()
