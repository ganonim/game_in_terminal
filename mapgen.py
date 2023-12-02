import json
import sys

while True:
    # Создание двухмерного масива
    MAP_SIZE = int(input("map size: "))
    if MAP_SIZE == 0:
        sys.exit()
    MAP_CHAR = input("char: ")
    DATA = [MAP_CHAR] * MAP_SIZE
    for i in range(MAP_SIZE):
        DATA[i] = [MAP_CHAR] * MAP_SIZE

    # Подсчет чисел слева от каждой строки
    for i in range(MAP_SIZE):
        # Подсчет текущего числа
        COUNT_STR = format(i, '02X')  # Форматирование чисел от 0 до FF
        DATA[i].insert(0, COUNT_STR)  # Вставка числа слева от строки масива

    # отображение масива
    for i, DATA in enumerate(DATA):
        print(*DATA)

    with open('data.json', 'w', encoding='utf8') as file:
        json.dump(DATA, file)
