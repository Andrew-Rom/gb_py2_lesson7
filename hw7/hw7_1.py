"""
HW 7-1
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

import os
import random as rnd
import shutil
import string
from itertools import chain

_DUMP_PATH_NAME = 'file_dump_dir'
_DUMP_SIZE = 30

_FILE_EXTENSIONS = {'videos': ('.mp4', '.wmv', '.avi', '.mov'),
                   'documents': ('.txt', '.rtf', '.doc', '.odt'),
                   'images': ('.gif', '.jpg', '.png', '.bmp')}


def create_full_dump(sourse_path: str =_DUMP_PATH_NAME, size: int =_DUMP_SIZE):
    extensions = list(chain.from_iterable([[extension for extension in value] for value in _FILE_EXTENSIONS.values()]))
    if os.path.exists(sourse_path):
        shutil.rmtree(sourse_path)
    os.mkdir(sourse_path)
    for _ in range(size):
        file_name = ''.join(rnd.choices(string.ascii_lowercase, k=rnd.randint(5, 10))) + rnd.choice(extensions)
        with open(os.path.join(sourse_path, file_name), 'w') as new_file:
            print('Some data', file=new_file)


def sort_files(file_dict=_FILE_EXTENSIONS, sourse_path: str = _DUMP_PATH_NAME):
    file_list = os.listdir(path=sourse_path)
    for dir_name, extensions in file_dict.items():
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
        os.mkdir(dir_name)
        for obj in file_list:
            if os.path.isfile(os.path.join(sourse_path, obj)) and os.path.splitext(obj)[1] in extensions:
                os.replace(os.path.join(os.getcwd(), sourse_path, obj), os.path.join(os.getcwd(), dir_name, obj))


if __name__ == '__main__':
    create_full_dump()
    sort_files()
