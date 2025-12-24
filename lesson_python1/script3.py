# Напишите скрипт, который выводит содержимое каталога, в котором мы находимся, и подсчитывает в нём количество файлов.
import os
current_directory = os.getcwd()
files = os.listdir(current_directory)
print("Текущий каталог:", current_directory)
print("Файлы в каталоге:", files)
print("Количество файлов в каталоге:", len(files))
