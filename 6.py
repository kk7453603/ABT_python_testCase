import json
import os
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class ChainData:
    id: int
    prev_item_id: Optional[int]
    next_item_id: Optional[int]
    data: str

    def to_dict(self):
        return {
            "id": self.id,
            "prev_item_id": self.prev_item_id,
            "next_item_id": self.next_item_id,
            "data": self.data
        }
    """Метод для сериализации в json"""


@dataclass
class Response:
    items: List[ChainData]
    total: int


def get_chain() -> Response:
    p = subprocess.Popen(["./chainTest"], stdout=subprocess.PIPE)
    r = json.loads(p.stdout.read())
    r['items'] = [ChainData(**c) for c in r['items']]
    return Response(**r)


def check_chain(filepath: Path) -> bool:
    status_code = os.system(f"./chainTest {filepath}")
    return status_code == 0


def solution(response: Response) -> Path:
    response.items.sort(key=lambda x: x.id)
    tmp=tempfile.NamedTemporaryFile(suffix='.json') #Создаем временный фал типа json
    with open(tmp.name, 'w', encoding='utf-8') as file:
        json.dump([item.to_dict() for item in response.items], file, indent=2)
    #Указываем способ сериализации
    return Path(tmp.name)


def main():
    response = get_chain()
    # Нужно восстановить цепочку элементов в порядке возрастания
    # например из get_chain пришли элементы (в items) [
    #                               ChainData(id=2, prev_item_id=None, next_item_id=3, data=''),
    #                               ChainData(id=1, prev_item_id=3, next_item_id=None, data=''),
    #                               ChainData(id=3, prev_item_id=2, next_item_id=1, data='')]
    # Из них получится цепочка [ChainData(id=2...), ChainData(id=3...), ChainData(id=1 ...)]
    # Получившуюся цепочку нужно вернуть в структуру Response и сохранить в json файл
    # путь до файла передать в check_chain

    filepath = solution(response)
    print(filepath)
    if check_chain(filepath): #Вылетает ошибка Can't open json file .Все шло хорошо, но я не понимаю как это пофиксить
        print("Success")
    else:
        print("Fail")


if __name__ == '__main__':
    main()
