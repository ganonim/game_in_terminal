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
    DATA = json.load(file)


def graphics():
    os.system('clear')
    DATA[HERO_Y][HERO_X] = "@"
    for i, DATA_MAP in enumerate(DATA):
        print(*DATA_MAP)


def move_hero(dx, dy):
    global HERO_X, HERO_Y
    HERO_X += dx
    HERO_Y += dy


while True:
    if GAME_START:
        GAME_START = False
        graphics()

    if keyboard.is_pressed('up') and not KEY_PRESSED:
        move_hero(0, -1)
        KEY_PRESSED = True
        graphics()
    if keyboard.is_pressed('down') and not KEY_PRESSED:
        move_hero(0, 1)
        KEY_PRESSED = True
        graphics()
    elif keyboard.is_pressed('left') and not KEY_PRESSED:
        move_hero(-1, 0)
        KEY_PRESSED = True
        graphics()
    elif keyboard.is_pressed('right') and not KEY_PRESSED:
        move_hero(1, 0)
        KEY_PRESSED = True
        graphics()
    elif keyboard.is_pressed('esc'):
        sys.exit()
    if not any(keyboard.is_pressed(key) for key in KEYS_TO_CHECK):
        KEY_PRESSED = False

    with open('data.json', 'r', encoding="utf-8") as file:
        DATA = json.load(file)
