# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
arr = [random.randint(-10, 10) for i in range(20)]
minimum = int(input('Введите нижнюю границу: '))
maximum = int(input('Введите верхнюю границу: '))
idx = []
print(arr)
for i in range(len(arr)):
    if minimum <= arr[i] <= maximum:
    	idx.append(i)
print(idx)        