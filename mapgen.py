import numpy as np
import noise
import json
import argparse
from colorama import Fore, init

# Инициализация colorama
init()

# Считывание цветов в формате HEX из файла colors.txt
with open('colors.txt', 'r') as file:
    colors_hex = file.read().splitlines()

# Преобразование значений HEX в ANSI escape-последовательности для установки цветов
colors_ansi = [f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:], 16)}m"
               for color in colors_hex]

symbols = ['≈', '~', '.', '-', '=', '#']

# Генерация шума Перлина с использованием seed
def generate_perlin_noise(map_size, scale, octaves, persistence, seed):
    perlin_img = np.zeros((map_size, map_size))

    for y in range(map_size):
        for x in range(map_size):
            perlin_img[x][y] = noise.pnoise2(x / scale, y / scale, octaves=octaves, persistence=persistence, base=seed)

    return perlin_img


def map_value_to_symbol(value, min_val, max_val):
    range_step = (max_val - min_val) / len(symbols)
    index = min(int((value - min_val) / range_step), len(symbols) - 1)
    return symbols[index]


def main(args):
    map_size = args.map_size
    height = args.height
    amplitude = args.amplitude
    scale = args.scale
    octaves = args.octaves
    persistence = args.persistence

    if map_size == 0:
        return

    # Задание случайного seed для генерации разного шума
    seed_value = np.random.randint(0, 1000)
    perlin_img = generate_perlin_noise(map_size, scale, octaves, persistence, seed_value)

    # Определение диапазона значений для маппинга к символам
    min_val = np.min(perlin_img)
    max_val = np.max(perlin_img)          

    # Создание списка символов на основе шума Перлина
    symbol_map = []
    for row in perlin_img:
        symbol_row = [map_value_to_symbol(val, min_val, max_val) for val in row]
        symbol_map.append(''.join(symbol_row))

    # Запись данных в файл в формате JSON
    with open('data.json', 'w', encoding="utf8") as file:
        json.dump(symbol_map, file)
    
    
    # Вывод символов с соответствующими цветами в формате ANSI escape-последовательностей
    for row in symbol_map:
        colored_row = [
            f"{colors_ansi[symbols.index(char) % len(colors_ansi)]}{char}\033[0m" if char in symbols else char
            for char in row
        ]
        print(*colored_row)
        
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Генерация шума Перлина и сохранение данных в JSON файл')
    parser.add_argument('-m', '--map_size', type=int, default=32, help='Determines the size '
                        'of the generated noise map. Higher values create larger maps with more detail.')
    parser.add_argument('--height', type=float, default=10.0, help='Sets average height'
                        ' in noise generation. Higher values elevate overall noise.')
    parser.add_argument('-a', '--amplitude', type=float, default=0.5, help='Controls'
                        ' intensity of Perlin noise. Higher values yield more pronounced variations.')
    parser.add_argument('-s', '--scale', type=float, default=10.0, help='Determines'
                        ' Perlin noise scale. Higher values generate larger features.')
    parser.add_argument('-o', '--octaves', type=int, default=6, help='Number of '
                        'octaves used. Affects noise detail.')
    parser.add_argument('-p', '--persistence', type=float, default=0.5, help='Influences '
                        'higher octave impact. Higher values maintain stronger octave influence.')

    args = parser.parse_args()
    main(args)
