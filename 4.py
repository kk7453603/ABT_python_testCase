import sys
import json


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    rounds=data["game"]["rounds"]
    question_count = sum(len(round_data["questions"]) for round_data in rounds)
    print(f"Number of questions: {question_count}")


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    rounds = data.get("game", {}).get("rounds", [])
    for round_data in rounds:
        questions = round_data.get("questions", [])
        for question in questions:
            correct_answer = question.get("correct_answer")
            print(f"Correct answer: {correct_answer}")


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    rounds = data.get("game", {}).get("rounds", [])
    max_time = float('-inf')
    for round_data in rounds:
        questions = round_data.get("questions", [])
        for question in questions:
            time_to_answer = question.get("time_to_answer",0)
            max_time = max(max_time, time_to_answer)
    print(f"Max answer time: {max_time}")


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)