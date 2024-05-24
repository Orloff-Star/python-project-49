from brain_games.scripts.functions import func


func.greeting()
name = input()
print("Hello, " + name)


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
    j = 1
    while j <= 3:
        num_one = func.random_number()
        num_two = func.random_number()
        list_div = max_divisor(num_one, num_two)
        max_div = max(list_div)
        print('Find the greatest common divisor of given numbers.')
        print(f"Question: {num_one}  {num_two}")
        answer_user = input('Your answer: ')
        if answer_user == str(max_div):
            print('Correct!')
            j += 1
        else:
            print(f"'{answer_user}'{func.incorrect_unswer} {max_div}.\
                \nLet's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    gcd()
