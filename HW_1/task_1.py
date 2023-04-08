# Была выполнена 1 задача из домашнего задания номер 1.

# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
 
number = int(input())
sum = 0
while number > 0:
    num = number % 10
    sum += num
    number = number // 10
print(sum)    
