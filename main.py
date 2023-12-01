import os
import json
import keyboard

with open('data.json', 'r') as file:
	data = json.load(file)

hero_x = 8
hero_y = 8
key_pressed = False
start = True

while True:
	def graphics():
		os.system('clear')
		data[hero_y][hero_x] = "@"
		for i in range(len(data)):
			for j in range(len(data[0])):
				print(data[i][j], end=" ")
			print()

	if start == True:
		start = False
		graphics()

	if keyboard.is_pressed('up') and not key_pressed:
		hero_y = hero_y-1
		key_pressed = True
		graphics()
	if keyboard.is_pressed('down') and not key_pressed:
		hero_y = hero_y+1
		key_pressed = True
		graphics()
	elif keyboard.is_pressed('left') and not key_pressed:
		hero_x = hero_x-1
		key_pressed = True
		graphics()
	elif keyboard.is_pressed('right') and not key_pressed:
		hero_x = hero_x+1
		key_pressed = True
		graphics()
	elif keyboard.is_pressed('esc'):
		exit()
	elif not keyboard.is_pressed('up') and not keyboard.is_pressed('down') and not keyboard.is_pressed('left') and not keyboard.is_pressed('right'):
		key_pressed = False

	with open('data.json', 'r') as file:
		data = json.load(file)


