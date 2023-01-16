# Напишите программу, удаляющую из текста все слова, содержащие 'абв'

# задаем начальные значения
pattern = 'абв'
my_str = 'абвкук привтттьт кУе ккабвжд имси ПАБвууц KJ'

# формируем новый список, разбивая строку по пробелам и фильруем его по паттерну, приведя элемент к строчным
my_str2 = list(filter(lambda rmv: pattern not in rmv.lower(), my_str.split()))

# выводим список в виде строки
print(*my_str2)
