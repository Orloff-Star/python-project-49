import random
from brain_games.scripts.functions import func


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
    specification = 'What number is missing in the progression?'
    list_progres = list_progression()
    hidden_num = random.randint(0, len(list_progres) - 1)
    correct_answer = list_progres[hidden_num]
    simbol = '..'
    list_progres[hidden_num] = simbol
    question = f'{list_progres}'
    return question, correct_answer, specification


def main():
    func.get_question_and_answer(progression)


if __name__ == '__main__':
    main()
