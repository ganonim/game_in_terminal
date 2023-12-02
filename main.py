import os
import json
import sys
import keyboard

KEYS_TO_CHECK = ['up', 'down', 'left', 'right']
HERO_X = 0
HERO_Y = 0
KEY_PRESSED = False
GAME_START = True

with open('data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

def graphics():
    os.system('clear')
    data[HERO_Y][HERO_X] = "@"
    for i, DATA_MAP in enumerate(data):
        print(*DATA_MAP)


def move_hero(dx, dy):
    global HERO_X, HERO_Y, data
    new_x = HERO_X + dx
    new_y = HERO_Y + dy
    if 0 <= new_x < len(data[0]) and 0 <= new_y < len(data):
        HERO_X = new_x
        HERO_Y = new_y
        graphics()


while True:
    if GAME_START:
        GAME_START = False
        graphics()

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
        if KEY_PRESSED:
            graphics()
    if keyboard.is_pressed('esc'):
        print("good byeee~~~")
        sys.exit()

    if not any(keyboard.is_pressed(key) for key in KEYS_TO_CHECK):
        KEY_PRESSED = False

    with open('data.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
