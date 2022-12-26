# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов,
# отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

while True:
    try:
       lst = list(map(float, input("Введите вещественные числа(через пробел):\n").split()))
       new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
       print(f'Разница между максимальным и минимальным значением дробной части элементов: {max(new_lst) - min(new_lst)}')
       break
    except ValueError:
        print('Ошибка, введите несколько чисел и хотя бы одно дробное число.')
