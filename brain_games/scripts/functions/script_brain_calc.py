#!/usr/bin/env python3


from brain_games.scripts.functions.func import get_question_and_answer
from brain_games.scripts.games import brain_calc


def main():
    get_question_and_answer(brain_calc)


if __name__ == '__main__':
    main()
