import os
import json
import time
import keyboard

with open('data.json', 'r') as file:
	data = json.load(file)

hero_x = 8
hero_y = 8
key_pressed = False


while True:
	if keyboard.is_pressed('up') and not key_pressed:
		hero_y = hero_y-1
		key_pressed = True
	if keyboard.is_pressed('down') and not key_pressed:
		hero_y = hero_y+1
		key_pressed = True
	elif keyboard.is_pressed('left') and not key_pressed:
		hero_x = hero_x-1
		key_pressed = True
	elif keyboard.is_pressed('right') and not key_pressed:
		hero_x = hero_x+1
		key_pressed = True
	elif keyboard.is_pressed('esc'):
		exit()

	elif not keyboard.is_pressed('up') and not keyboard.is_pressed('down') and not keyboard.is_pressed('left') and not keyboard.is_pressed('right'):
		key_pressed = False

	os.system('clear')
	data[hero_y][hero_x] = "@"
	for i in range(len(data)):
		for j in range(len(data[0])):
			print(data[i][j], end=" ")
		print()

	with open('data.json', 'r') as file:
		data = json.load(file)
	#time.sleep(0.1)
