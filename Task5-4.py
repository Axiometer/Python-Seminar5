# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def rle_encode(rawstring):
    encoded = '' 
    prev_char = '' 
    count = 1
    # если строка пустая возвращаем пусто
    if not rawstring: 
        return '' 
    for char in rawstring: 
        # если текущий символ не совпадает с предыдущим
        if char != prev_char: 
            # тогда добаляем количество и символ
            if prev_char: 
                encoded += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            # иначе добавляем количество
            count += 1 
    else: 
        # закончили сжатие
        encoded += str(count) + prev_char 
    return encoded

def rle_decode(encodedstring):
    decode = ''
    count = ''
    for char in encodedstring:
        # если символ - цифра
        if char.isdigit():
            # добавляем к количеству
            count += char
        else:
            # иначе символ, значит записываем символ count раз
            decode += char * int(count)
            count = ''
    return decode

def main():
    print('Изначальная строка данных:')
    rawtext = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZEEEEEEEEEEEEEEEEEEEEEEEEERGSSSSSSSSSSSSSS'
    print(rawtext)
    print()

    print('Сжатая строка данных:')
    compressed_text = rle_encode(rawtext) 
    print(compressed_text)
    print()

    print('Распакованная строка:')
    decompressed_text = rle_decode(compressed_text)
    print(decompressed_text)

if __name__ == '__main__':
    main()