import sys
import json


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    raise NotImplementedError


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    raise NotImplementedError


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    raise NotImplementedError


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки

    main(filename)
