import json

a = int(input("map size: "))
data = ['.'] * a
for i in range(a):
    data[i] = ['.'] * a
print(data)

with open('data.json', 'w', encoding='utf8') as file:
    json.dump(data, file)
