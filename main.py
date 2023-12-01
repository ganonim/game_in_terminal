import os
import json
import time
import keyboard

with open('data.json', 'r') as file:
	data = json.load(file)

hero_x = 8
hero_y = 8

while True:
	if keyboard.is_pressed('up'):
		hero_y = hero_y-1
	elif keyboard.is_pressed('down'):
		hero_y = hero_y+1
	elif keyboard.is_pressed('left'):
		hero_x = hero_x-1
	elif keyboard.is_pressed('right'):
		hero_x = hero_x+1
	elif keyboard.is_pressed('esc'):
		exit()

	os.system('clear')
	data[hero_y][hero_x] = "@"
	for i in range(len(data)):
		for j in range(len(data[0])):
			print(data[i][j], end=" ")
		print()

	with open('data.json', 'r') as file:
		data = json.load(file)
	time.sleep(0.1)
