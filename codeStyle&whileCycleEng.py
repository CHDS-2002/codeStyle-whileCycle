# os - library for working with the console

import os

# Setting the font color of the console
os.system('COLOR B')

# Let's set a list
numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
value = numbers[0]
i = 0

# Let's output the positive elements of the array
print('\nArray elements:')

while value >= 0:
    i += 1

    if value > 0:
        print(value)
    elif numbers[i] < 0:
        break

    value = numbers[i]

print()

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
