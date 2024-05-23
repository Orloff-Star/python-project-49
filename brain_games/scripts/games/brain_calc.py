from brain_games.scripts.functions import func


func.greeting()
name = input()
print("Hello, " + name)


def calc():
    i = 0
    while i < 3:
        number_one = func.random_number()
        number_two = func.random_number()
        calculat = f"{number_one} {func.choose_operator()} {number_two}"
        result = eval(calculat)
        print('What is the result of the expression?')
        print(f"Question: {calculat}")
        answer_user = input('Your answer: ')
        if answer_user == str(result):
            print('Correct!')
            i += 1
        else:
            print(f"""'{answer_user}'{func.incorrect_unswer} {result}.
            \nLet's try again, {name}!""")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    calc()
