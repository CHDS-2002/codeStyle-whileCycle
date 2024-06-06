# os - библиотека для работы с консолью

import os

# Зададим цвет шрифта консоли
os.system('COLOR B')

# Зададим список
numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
value = numbers[0]
i = 0

# Выведем положительные элементы массива
print('\nЭлементы массива:')

while value >= 0:
    i += 1

    if value > 0:
        print(value)
    elif numbers[i] < 0:
        break

    value = numbers[i]

print()

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
