import json
import numpy as np
import sys
import noise

symbols = [' ', '.', '-', '=', '#']


# Генерация шума Перлина с использованием seed
def generate_perlin_noise(map_size, scale, octaves, persistence, seed):
    perlin_img = np.zeros((map_size, map_size))

    for y in range(map_size):
        for x in range(map_size):
            perlin_img[x][y] = noise.pnoise2(x / scale, y / scale, octaves=octaves, persistence=persistence, base=seed)

    return perlin_img


while True:
    map_size = int(input("Map size: "))
    if map_size == 0:
        sys.exit()

    # Задание случайного seed для генерации разного шума
    seed_value = np.random.randint(0, 1000)
    perlin_img = generate_perlin_noise(map_size, 10.0, 6, 0.5, seed_value)

    # Определение диапазона значений для маппинга к символам
    min_val = np.min(perlin_img)
    max_val = np.max(perlin_img)

    # Создание маппинга значений массива шума Перлина к символам
    def map_value_to_symbol(value):
        range_step = (max_val - min_val) / len(symbols)
        index = min(int((value - min_val) / range_step), len(symbols) - 1)
        return symbols[index]

    # Создание списка символов на основе шума Перлина
    symbol_map = []
    for row in perlin_img:
        symbol_row = [map_value_to_symbol(val) for val in row]
        symbol_map.append(''.join(symbol_row))
    
    # Запись данных в JSON файл
    with open('data.json', 'w', encoding='utf8') as file:
        json.dump(symbol_map, file)

    # Создание изображения с символами
    for i, DATA_MAP in enumerate(symbol_map):
        print(*DATA_MAP)
