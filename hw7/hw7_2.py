"""
HW 7-2
Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов (при переименовании в конце имени добавляется порядковый номер).
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os

from hw7_1 import create_full_dump as get_dump

_PATH_NAME = 'dump_dir'
_DUMP_SIZE = 30


def group_rename(sourse_extension: str,
                 result_extension: str,
                 sourse_path=_PATH_NAME,
                 default_file_name: str = '-renamed_file',
                 len_order_num: int = 3,
                 len_save_name: list[int, int] = [2, 5]):
    all_files = os.listdir(sourse_path)
    file_list = list(filter(lambda file: os.path.splitext(file)[1] == sourse_extension, all_files))
    numerated_file_list = {}
    for i, file in enumerate(file_list, start=1):
        if len(str(i)) < len_order_num:
            number = str('0') * (len_order_num - len(str(i))) + str(i)
        else:
            number = str(i)
        numerated_file_list.update({file: number})

    for file, number in numerated_file_list.items():
        old_file_name = os.path.splitext(file)[0]
        if len(old_file_name) <= len_save_name[0]:
            new_file_name = default_file_name + number + result_extension
        elif len(old_file_name) <= len_save_name[1]:
            new_file_name = old_file_name[len_save_name[0] - 1:] \
                            + default_file_name + number + result_extension
        else:
            new_file_name = old_file_name[len_save_name[0] - 1: len_save_name[1] - 1] \
                            + default_file_name + number + result_extension
        numerated_file_list.update({file: new_file_name})

    os.chdir(sourse_path)
    for old_file, new_file in numerated_file_list.items():
        os.rename(old_file, new_file)


if __name__ == '__main__':
    get_dump(sourse_path=_PATH_NAME, size=_DUMP_SIZE)
    group_rename(sourse_extension='.txt', result_extension='.rnf')
