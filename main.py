import os
from os.path import abspath, normpath


# #1 задание
# absolutePath= os.path.abspath("test_file_1")
# # print(normpath(absolutePath)) # нормализация абсолютного пути

# второе задание  вывести на экран содержимое папки вашего проекта
# в задании не указано какой то конкретной папки
# поэтому я вывел основную папку проекта

# 2 задание
# for dirpath ,dirnames ,filenames   in os.walk("."):
#     print(dirpath,"пути к директории")
#     print(dirnames,"имена")
#     print(filenames,"названия файлов")
#
# 3 длиновато получилась строка
#print(normpath(abspath(os.path.join(r".\folder_data2", "test_file_3", ))))

# 4 задание
# для удобства через функции сделал хоть в задании и не указано
#
# def create_dir(directory_to_crate):
#
#     if  directory_to_crate not in os.listdir():
#         os.mkdir(directory_to_crate)
#         print("создано")
#     else:
#         print("нельзя создать ")
#
#
# def delet_dir(directory_to_del):
#     if directory_to_del in os.listdir():
#         os.rmdir(directory_to_del)
#         print("удалено")
#     else:
#         print("такого файла нет")
#
# create_dir("data_path_2")
# delet_dir("data_path_2")
#


# 2 задача

text_to_write ="""Если б мишки были пчелами,
То они бы нипочем,
Никогда и не подумали,
Так высоко строить дом."""
def write_file(filename,text_to_write):
    with open(filename,"w",encoding="utf-8") as f:
        f.write(text_to_write)
def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

write_file("stishok",text_to_write)
read_file("stishok")