import json
import sys
import random

# Словарь символов и их вероятностей
symbols_probabilities = {
    '.': 0.4,  # Пример вероятности для символа "."
    '#': 0.2,  # Пример вероятности для символа "#"
    ',': 0.4,  # Пример вероятности для символа ","
    '*': 0.3,  # Пример вероятности для символа "*"
    '%': 0.1,   # Пример вероятности для символа "@"
    '0': 0.1
}

while True:
    # Создание двумерного массива
    map_size = int(input("Map size: "))
    if map_size == 0:
        sys.exit()

    data = []

    # Генерация случайных символов с учетом вероятностей
    for i in range(map_size):
        row = [random.choices(list(symbols_probabilities.keys()), weights=list(symbols_probabilities.values()))[0] for _ in range(map_size)]
#        count_str = format(i, '02X')  # Форматирование чисел от 0 до FF
#        row.insert(0, count_str)  # Вставка числа слева от строки массива
        data.append(row)

    # Отображение массива
    for row in data:
        print(*row)

    # Запись данных в JSON файл
    with open('data.json', 'w', encoding='utf8') as file:
        json.dump(data, file)
