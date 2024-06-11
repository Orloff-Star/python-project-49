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


def get_progression(start, step, length):
    end = start + (length * step)
    result_list = []
    for i in range(start, end, step):
        result_list.append(i)
    return result_list


def generate_question_answer():
    random_index = random.randint(START_INDEX, END_INDEX)
    random_step = random.randint(START_STEP, END_STEP)
    random_length = random.randint(START_LENGHT, END_LENGHT)
    progression = get_progression(random_index, random_step, random_length)
    hidden_num = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_num]
    empty_symbol = ".."
    progression[hidden_num] = empty_symbol
    question = f'{progression}'
    return question, str(correct_answer)
