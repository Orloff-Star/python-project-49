import random


name = ''
print("Welcome to the Brain Games!")
print('May I have your name? ', end='')
name = input()
print("Hello, " + name)


def brain_even():
    answer_yes = 'yes'
    answer_no = 'no'
    i = 0
    while i < 3:
        random_number = random.randrange(0, 100)
        print('Answer "yes" if the number is even, otherwise answer "no"')
        print(f"Question: {random_number}")
        answer_user = input('Your answer: ').lower()
        if random_number % 2 == 0 and answer_user == answer_yes or random_number % 2 != 0 and answer_user == answer_no:
            print('Correct!')
            i += 1
        else:
            if answer_user == answer_yes:
                print(f"'{answer_user}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
                break
            else:
                print(f"'{answer_user}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
                break
    else: print(f"Congratulations, {name}!")

if __name__ == "__main__":
    brain_even()
