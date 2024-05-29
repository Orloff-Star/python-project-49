import random
from brain_games.scripts.functions import func


func.greeting()
name = input()
print("Hello, " + name)


def prime_num(num):
    if num <= 1:
        return False
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


def prime():
    answer_yes = 'yes'
    answer_no = 'no'
    i = 0
    while i < 3:
        random_number = random.randrange(0, 300)
        correct_answer = prime_num(random_number)
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print(f"Question: {random_number}")
        answer_user = input('Your answer: ').lower()
        if correct_answer is True and answer_user == answer_yes \
                or correct_answer is False and answer_user == answer_no:
            print('Correct!')
            i += 1
        else:
            if answer_user == answer_yes:
                print(f"'{answer_user}'{func.incorrect_unswer} {answer_no}.\
                \nLet's try again, {name}!")
                break
            else:
                print(f"'{answer_user}'{func.incorrect_unswer} {answer_yes}.\
                \nLet's try again, {name}!")
                break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    prime()
