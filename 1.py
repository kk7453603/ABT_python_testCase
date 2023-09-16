import os
from math import ceil

def black_book(page: int) -> bool:
    status_code = os.system(f"./black-book -n {page}")
    return status_code == 0

"""Странное условие с последней страницей. Как я понял, True означает наличие страницы в книге, а False - 
отсутствие, на этом и строил свой алгоритм"""
def find_last_page(): #бинарный поиск наиболее быстрый алгоритм для поиска упорядоченных чисел на интервале
    lower_bound = 1
    upper_bound = 10000000 # so much

    while lower_bound < upper_bound:
        mid = ceil((lower_bound + upper_bound) / 2)
        if black_book(mid):
            lower_bound = mid
        else:
            upper_bound = mid - 1

    return lower_bound

def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.
    
    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_book) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.
    
    Уточнение:
        black_book возвращает True, если страница последняя
                  возвращает False, если страница не последняя.
    
    
    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    # тут явно нужен алгоритм
    last_page = find_last_page()
    print("Номер последней страницы:", last_page)


if __name__ == '__main__':
    main()

