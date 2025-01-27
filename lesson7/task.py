"""Задание 1: Операции с кортежами

Условие: Создайте кортеж, содержащий три целых числа.
Выведите на экран каждое число, а затем выведите их сумму."""

my_tuple = (2, 4, 6)

print(f'Первое число: {my_tuple[0]}')
print(f'Второе число: {my_tuple[1]}')
print(f'Третье число: {my_tuple[2]}')
print(f'Сумма: {sum(my_tuple)}')

"""Задание 1: Работа со списками и множествами

Условие: Вводятся два списка чисел, числа вводятся вручную. 
Выведите, сколько чисел содержится одновременно как в первом списке, 
так и во втором."""

list1 = set(input('Введите первый список: ').split())
list2 = set(input('Введите второй список: ').split())

print(f'Количество пересечений: {len(list1 & list2)}')
