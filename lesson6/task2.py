"""1 Задание. Код с использованием while:
Программа запрашивает у пользователя некоторое целое число,
после чего использует while,
чтобы вывести на экран все числа от 0 до введенного числа включительно.
Переменная i инициализируется значением 0,
а затем на каждой итерации цикла проверяется условие i <= n.
Если оно выполнено, то на экран выводится текущее значение переменной i,
после чего значение i увеличивается на 1. Цикл продолжается,
пока i не станет больше n.
"""
num = int(input('Введите целое число: '))
i = 0
while i <= num:
    print(i)
    i += 1