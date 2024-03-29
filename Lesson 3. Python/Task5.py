# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fib(n):
    if n > -1:
        if n == 0 or n == 1:
            return n
        else:
            return fib(n-1) + fib(n-2)
    if n <= -1:
        return (((-1) ** ((abs(n)+1))) * fib(abs(n)))

# while True:
#     try:
#        k = int(input('\nВведите число: '))
#        for i in range(-k, k+1):
#             print(fib(i), end=', ')
#
#     except:
#         print('Ошибка, это не число.')

k = int(input('Введите число: '))
new_list = [fib(i) for i in range(-k, k+1)]  # со списком разобрался
print(new_list)