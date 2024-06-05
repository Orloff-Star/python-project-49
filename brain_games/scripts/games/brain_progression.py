import random


SPECIFICATION = 'What number is missing in the progression?'


def is_list_progression():
    random_index = random.randint(0, 200)
    random_step = random.randint(1, 10)
    random_length = random.randint(7, 10)
    list_progression = list(range(0, 300))
    result_list = []
    for i in range(random_index, len(list_progression), random_step):
        result_list.append(i)
    result_list = result_list[0:random_length]
    return result_list


def user_interaction():
    list_progres = is_list_progression()
    hidden_num = random.randint(0, len(list_progres) - 1)
    correct_answer = list_progres[hidden_num]
    simbol = ".."
    list_progres[hidden_num] = simbol
    string = ''
    for el in list_progres:
        string += str(el)
        string += ' '
    question = f'{string}'
    return question, correct_answer
