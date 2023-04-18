# Была выполнена 2 задача из домашнего задания номер 3.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X.

import random
N = int(input('Введите длину массива: '))
arr_A = [random.randint(-50, 50) for i in range(N)]
print(arr_A)
x = int(input('Введите искомое число: '))

if x in arr_A:
    print(x)
else:
    arr_A.append(x)
    unique_arr_A = list(sorted(set(arr_A)))
    position_x = unique_arr_A.index(x)

    if position_x == N:
        print(unique_arr_A[position_x - 1])
    elif position_x == 0:
        print(unique_arr_A[position_x + 1])
    else:
        position_before = position_x - 1
        position_after = position_x + 1
        print([unique_arr_A[position_before], unique_arr_A[position_after]]
              [unique_arr_A[position_x] - unique_arr_A[position_before] > unique_arr_A[position_after] - unique_arr_A[position_x]])
