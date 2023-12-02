import os
import json
import sys
import keyboard

HERO_X = 8
HERO_Y = 8
KEY_PRESSED = False
GAME_START = True

with open('data.json', 'r', encoding="utf-8") as file:
    DATA = json.load(file)

while True:
    def Graphics():
        os.system('clear')
        DATA[HERO_Y][HERO_X] = "@"
        for i, DATA_MAP in enumerate(DATA):
            print(*DATA_MAP)

    if GAME_START is True:
        GAME_START = False
        Graphics()

    if keyboard.is_pressed('up') and not KEY_PRESSED:
        HERO_Y = HERO_Y-1
        KEY_PRESSED = True
        Graphics()
    if keyboard.is_pressed('down') and not KEY_PRESSED:
        HERO_Y = HERO_Y+1
        KEY_PRESSED = True
        Graphics()
    elif keyboard.is_pressed('left') and not KEY_PRESSED:
        HERO_X = HERO_X-1
        KEY_PRESSED = True
        Graphics()
    elif keyboard.is_pressed('right') and not KEY_PRESSED:
        HERO_X = HERO_X+1
        KEY_PRESSED = True
        Graphics()
    elif keyboard.is_pressed('esc'):
        sys.exit()
    elif not keyboard.is_pressed('up') and not \
            keyboard.is_pressed('down') and not \
            keyboard.is_pressed('left') and not \
            keyboard.is_pressed('right'):
        KEY_PRESSED = False

    with open('data.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
