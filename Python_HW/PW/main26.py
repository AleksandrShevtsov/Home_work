# import sys
# args = sys.argv
# print(args)
#
# name = 'Anonim'
# if len(args) > 1:
#     name = args[1]
# print(f'Hello, {name}')


# import sys
# print('Список параметров, переданных скрипту')
# print(sys.argv)
# print([arg for arg in sys.argv if arg[0] != '-'])



# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='Path to input file')
# parser.add_argument('--output', help='Path to output file')
# args = parser.parse_args()
# print(args.input)
# print(args.output)


# import os
# current_dir = os.getcwd()
# # print(current_dir)
# os.chdir('files')
#
# current_dir = os.getcwd()
# # print(current_dir)

# files = os.listdir(current_dir)
# # print(files)
# # os.mkdir('new_directory')
# # os.makedirs('new_directory/sub_directory')
# for dirpath, dirnames, filenames in os.walk(current_dir):
#     for filename in filenames:
#         # print(filename)
#         # print(dirpath)
#         # print(dirnames)
#         print(os.path.join(dirpath, filename))
#
# import os
#
# path = os.path.join('/path/to', 'file.txt')
# print(path)
# absolute_path = os.path.abspath(path)
# print(absolute_path)
# print(os.getcwd())
# exists = os.path.exists(absolute_path)
# print(exists)
# is_directory = os.path.isdir(absolute_path)
# print(is_directory)
# is_file = os.path.isfile(absolute_path)
# print(is_file)


import os
# def process_directory(directory):
#     for name in os.listdir(directory):
#         file_path = os.path.join(directory, name)
#         if os.path.isfile(file_path):
#             # Обработка файла
#             print(os.path.abspath(file_path))
#         elif os.path.isdir(file_path):
#         # Рекурсивный вызов для вложенного каталога
#             process_directory(file_path)
# start_directory = 'files'
# process_directory(start_directory)



import os
import sys

def find_txt(directory):
    for entry in os.scandir(directory):
        if entry.is_file() and entry.name.endswith('.txt'):
            txt_file.append(entry.name)
        elif entry.is_dir():
            find_txt(entry.path)

txt_file = []
args = sys.argv
find_txt(args[1])
# find_txt('files')
print(txt_file)

