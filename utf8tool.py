import argparse

def convert_to_symbol(unicode_code):
    try:
        unicode_value = int(unicode_code, 16)  # Переводим шестнадцатеричное значение в число
        symbol = chr(unicode_value)  # Получаем символ из Unicode-кода
        return symbol
    except ValueError:
        return "Неверный Unicode-код"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Конвертер Unicode-кода в символ')
    parser.add_argument('unicode_code', help='Unicode-код символа в шестнадцатеричном формате')

    args = parser.parse_args()
    symbol = convert_to_symbol(args.unicode_code)
    print(f"Символ: {symbol}")
