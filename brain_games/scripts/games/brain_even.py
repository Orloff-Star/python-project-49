import random
from brain_games.scripts.functions import func


func.greeting()
name = input()
print("Hello, " + name)


def even():
    answer_yes = 'yes'
    answer_no = 'no'
    i = 0
    while i < 3:
        random_number = random.randrange(0, 100)
        print('Answer "yes" if the number is even, otherwise answer "no"')
        print(f"Question: {random_number}")
        answer_user = input('Your answer: ').lower()
        if random_number % 2 == 0 and answer_user == answer_yes \
                or random_number % 2 != 0 and answer_user == answer_no:
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
    even()
