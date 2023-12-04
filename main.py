import os
import json
import sys
import keyboard
from colorama import Fore, init

KEYS_TO_CHECK = ['up', 'down', 'left', 'right']
symbols = ['≈', '~', '.', '-', '=', '#']
SYMBOL_HERO = '@'
HERO_X = 0
HERO_Y = 0
KEY_PRESSED = False
GAME_START = True

init()

# Считывание цветов в формате HEX из файла colors.txt
with open('colors.txt', 'r') as file:
    colors_hex = file.read().splitlines()

# Преобразование значений HEX в ANSI escape-последовательности для установки цветов
colors_ansi = [f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:], 16)}m"
               for color in colors_hex]

# Считывание данных игры из data.json
with open('data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)


def graphics():
    os.system('clear')
    row = data[HERO_Y]
    data[HERO_Y] = row[:HERO_X] + SYMBOL_HERO + row[HERO_X + 1:]
    for row in data:
        colored_row = [
            f"{colors_ansi[symbols.index(char) % len(colors_ansi)]}{char}\033[0m" if char in symbols else char
            for char in row]
        print(*colored_row)


graphics()


def move_hero(dx, dy):
    global HERO_X, HERO_Y
    new_x = HERO_X + dx
    new_y = HERO_Y + dy
    if 0 <= new_x < len(data[0]) and 0 <= new_y < len(data):
        HERO_X = new_x
        HERO_Y = new_y
        graphics()


while True:

    if not KEY_PRESSED:
        if keyboard.is_pressed('up'):
            move_hero(0, -1)
            KEY_PRESSED = True
        elif keyboard.is_pressed('down'):
            move_hero(0, 1)
            KEY_PRESSED = True
        elif keyboard.is_pressed('left'):
            move_hero(-1, 0)
            KEY_PRESSED = True
        elif keyboard.is_pressed('right'):
            move_hero(1, 0)
            KEY_PRESSED = True
    if keyboard.is_pressed('esc'):
        print("good byeee~~~")
        sys.exit()

    if not any(keyboard.is_pressed(key) for key in KEYS_TO_CHECK):
        KEY_PRESSED = False

    with open('data.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
