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

DUMP_PATH_NAME = 'file_dump_dir'

FILE_EXTENSIONS = {'videos': ('.mp4', '.wmv', '.avi', '.mov'),
                   'documents': ('.txt', '.rtf', '.doc', '.odt'),
                   'images': ('.gif', '.jpg', '.png', '.bmp')}


def create_full_dump():
    extensions = list(chain.from_iterable([[extension for extension in value] for value in FILE_EXTENSIONS.values()]))
    if os.path.exists(DUMP_PATH_NAME):
        shutil.rmtree(DUMP_PATH_NAME)
    os.mkdir(DUMP_PATH_NAME)
    for _ in range(30):
        file_name = ''.join(rnd.choices(string.ascii_lowercase, k=rnd.randint(5, 10))) + rnd.choice(extensions)
        with open(os.path.join(DUMP_PATH_NAME, file_name), 'w') as new_file:
            print('Some data', file=new_file)


create_full_dump()
