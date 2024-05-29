import random
from brain_games.scripts.functions import func


func.greeting()
name = input()
print("Hello, " + name)


def list_progression():
    random_index = random.randint(0, 200)
    random_step = random.randint(1, 10)
    random_length = random.randint(7, 10)
    list_progression = list(range(0, 300))
    result_list = []
    for i in range(random_index, len(list_progression), random_step):
        result_list.append(i)
    result_list = result_list[0:random_length]
    return result_list


def progression():
    j = 1
    while j <= 3:
        list_progres = list_progression()
        hidden_num = random.randint(0, len(list_progres) - 1)
        search_element = list_progres[hidden_num]
        simbol = '..'
        list_progres[hidden_num] = simbol
        print('What number is missing in the progression?')
        print(f"Question: {list_progres}")
        answer_user = input('Your answer: ')
        if answer_user == str(search_element):
            print('Correct!')
            j += 1
        else:
            print(f"'{answer_user}'{func.incorrect_unswer} {search_element}.\
                \nLet's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    progression()
