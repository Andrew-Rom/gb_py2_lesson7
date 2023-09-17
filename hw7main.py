from hw7 import create_full_dump, sort_files, group_rename

create_full_dump(sourse_path='dir_for_hw7-1')
sort_files(sourse_path='dir_for_hw7-1')

create_full_dump(sourse_path='dir_for_hw7-2')
group_rename(sourse_path='dir_for_hw7-2', sourse_extension='.txt', result_extension='.rnf')
