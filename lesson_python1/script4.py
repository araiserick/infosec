import os

parameter = input("Введите путь к файлу или каталогу: ")
if os.path.exists(parameter):
    if os.path.isfile(parameter):
        print(f"{parameter} - это файл.")
    elif os.path.isdir(parameter):
        print(f"{parameter} - это каталог.")
else:
    print(f"{parameter} - не существует.")