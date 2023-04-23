# Задача № 2 из домашнего задания № 5.
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2    4 

def sum(a, b):
    if a == 0:
        return b
    return sum(a - 1, b + 1)

a = int(input('Введите первое положительное число: ')) 
b = int(input('Введите второе положительное число: '))
print(f"sum({a}, {b}) = {sum(a, b)}")