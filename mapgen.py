import json

a = int(input("map size: "))
data = ['.'] * a
for i in range(a):
    data[i] = ['.'] * a
print(data)

with open('data.json', 'w') as file:
	json.dump(data, file)
