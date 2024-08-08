import os
from datetime import datetime

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        # путь файла
        filepach = os.path.join(file)
        # размер файла
        filesize = os.path.getsize(file)
        # время изменения файла
        filetime = os.path.getmtime(file)
        formatted_time = datetime.fromtimestamp(filetime)
        # родительская директория
        parent_dir = os.path.dirname(os.path.abspath(file))
print(f'Обнаружен файл: {file}, Путь: {filepach}, Размер: {filesize} байт, Время изменеия: {formatted_time},'
      f' Родительская директория: {parent_dir}')
