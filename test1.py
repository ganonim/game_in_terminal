symbol_map = [
    "-.  ....----..-=",
    "=------======-==",
]

# Координаты символа для замены
x = 1
y = 0

# Символ для замены
new_symbol = "@"  # Новый символ для замены

# Проверяем, чтобы индексы были в пределах размеров массива
if 0 <= y < len(symbol_map) and 0 <= x < len(symbol_map[y]):
    row = symbol_map[y]
    symbol_map[y] = row[:x] + new_symbol + row[x + 1:]

# Вывод обновленного массива
for row in symbol_map:
    print(row)
