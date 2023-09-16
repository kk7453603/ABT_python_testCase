import os
import re
from concurrent.futures import ThreadPoolExecutor


def find_emails(path):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails=[]
    with open(path, 'r') as f:
        content = f.read()
        emails.extend(re.findall(email_pattern, content)) #Использование регулярного выражения для поиска почты
    return emails


def task1():
    # в папке test найти все файлы filenames вывести количество
    counter = 0
    for root, dirs, files in os.walk("./test", topdown=False):
        for file in files:
            if "filenames" in file:  # Нахожу все файлы, содержащие подстроку filenames
                counter += 1
    print(f'Количество файлов filenames в подпапках test - {counter}')


def task2():
    # в папке test найти все email адреса записанные в файлы
    file_paths = []
    emails=[]
    for root, dirs, files in os.walk("./test", topdown=False):
        for file in files:
            file_paths.append(os.path.join(root, file))

    with ThreadPoolExecutor() as ext: #Используется многопоточность
        res=ext.map(find_emails,file_paths) #Функция аналогична стандартной map(), но с параллельным выполнением
        for el in res:
            emails.extend(el)

    for email in emails:
        print(f'email: {email}')
def main():
    task1()
    task2()
    # дополнительно: придумать над механизмом оптимизации 2-й задачи (параллелизация)


if __name__ == '__main__':
    main()
