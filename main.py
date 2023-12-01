import os
import getpass
import socket

# map
x = 8
y = 8

# graphic
for i in range(1, y+1):
	for j in range(1, x+1):
		if i == 1:
			print(chr(63+j), end=" ")
		elif j == 1:
			print(i-2, end=" ")
		else:
			print("$", end=" ")
	print()

# comander
usr = getpass.getuser()
hostname = socket.gethostname()
current_directory = os.getcwd()
a = input(usr + "$" + hostname + " ~" + current_directory +" > ")

# input comand
if a == "bye" or "exit":
	print("good bueee~")
	exit()
elif a == "set":
	
