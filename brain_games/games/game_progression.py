import random


SPECIFICATION = 'What number is missing in the progression?'
START_INDEX = 0
END_INDEX = 200
START_STEP = 1
END_STEP = 10
START_LENGHT = 7
END_LENGHT = 10
START_LIST = 0
END_LIST = 300


def get_progression():
    random_index = random.randint(START_INDEX, END_INDEX)
    random_step = random.randint(START_STEP, END_STEP)
    random_length = random.randint(START_LENGHT, END_LENGHT)
    list_progression = list(range(START_LIST, END_LIST))
    result_list = []
    for i in range(random_index, len(list_progression), random_step):
        result_list.append(i)
    result_list = result_list[0:random_length]
    return result_list


def ask_question_get_answer():
    progression = get_progression()
    hidden_num = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_num]
    empty_symbol = ".."
    progression[hidden_num] = empty_symbol
    result = ''
    for el in progression:
        result += str(el)
        result += ' '
    question = f'{result}'
    return question, correct_answer
