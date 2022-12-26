# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as r

num = []
for i in range(5):
    num.append(r(0, 10))

count = 0
for i in range(len(num)):
    if i % 2 != 0:
        count += num[i]

print(num)
print(count)
